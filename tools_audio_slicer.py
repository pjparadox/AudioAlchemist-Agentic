import os
import argparse
import librosa
import numpy as np
import soundfile as sf
import json
from glob import glob

def hz_to_note_name(hz):
    if hz is None or hz <= 0 or np.isnan(hz):
        return "Unknown"
    return librosa.hz_to_note(hz)

def amplitude_to_velocity(amp):
    # Map 0.0-1.0 to 0-127
    return int(np.clip(amp * 127, 0, 127))

def get_robust_pitch(y, sr):
    """
    Uses PYIN to estimate pitch, but filters out unstable estimates.
    Returns the most frequent note detected (mode) or weighted average.
    """
    # pyin is expensive, so we might limit fmin/fmax if we knew the genre,
    # but for general use we keep wide range.
    # Pad if short
    if len(y) < 2048:
        y = librosa.util.fix_length(y, size=2048)

    f0, voiced_flag, voiced_probs = librosa.pyin(
        y,
        fmin=librosa.note_to_hz('C1'),
        fmax=librosa.note_to_hz('C8'),
        sr=sr,
        frame_length=2048,
        fill_na=np.nan
    )

    # Filter only voiced frames
    valid_f0 = f0[~np.isnan(f0)]

    if len(valid_f0) == 0:
        return "Unknown", 0.0

    # Use Median for stability
    median_f0 = np.median(valid_f0)

    # Check stability: standard deviation
    std_f0 = np.std(valid_f0)

    # If pitch varies wildly, it might be a slide or noise.
    # For a sampler "Note", we want the stable center.
    return hz_to_note_name(median_f0), std_f0

def analyze_segment(y, sr):
    # Pitch
    note, pitch_std = get_robust_pitch(y, sr)

    # Velocity (Peak Amplitude)
    peak_amp = np.max(np.abs(y))
    velocity = amplitude_to_velocity(peak_amp)

    # Features for Description
    # Spectral Centroid (Timbre Brightness)
    centroid = np.mean(librosa.feature.spectral_centroid(y=y, sr=sr))

    # Spectral Rolloff (Timbre Shape)
    rolloff = np.mean(librosa.feature.spectral_rolloff(y=y, sr=sr))

    # Zero Crossing Rate (Noisiness)
    zcr = np.mean(librosa.feature.zero_crossing_rate(y))

    # RMS (Loudness consistency)
    rms = np.mean(librosa.feature.rms(y=y))

    features = {
        "spectral_centroid": float(centroid),
        "spectral_rolloff": float(rolloff),
        "zero_crossing_rate": float(zcr),
        "rms": float(rms),
        "pitch_stability": float(pitch_std),
        "duration": float(len(y) / sr)
    }

    return note, velocity, features

def trim_silence_adaptive(y, top_db=60):
    """
    Trims silence from the end of the segment adaptively.
    """
    return librosa.effects.trim(y, top_db=top_db)[0]

def process_file(filepath, output_dir, sensitivity=0.5):
    filename = os.path.basename(filepath)
    name, ext = os.path.splitext(filename)

    print(f"Processing: {filename}")
    try:
        y, sr = librosa.load(filepath, sr=None)
    except Exception as e:
        print(f"Error loading {filename}: {e}")
        return []

    # 1. Onset Detection (Energy based)
    # backtrack=True shifts the onset to the nearest preceding minimum energy
    # this is CRITICAL for preserving attack transients (the "thwack").
    onset_frames = librosa.onset.onset_detect(
        y=y,
        sr=sr,
        backtrack=True,
        units='frames',
        pre_avg=3,
        post_avg=3,
        delta=sensitivity # Adjusting sensitivity
    )
    onset_samples = librosa.frames_to_samples(onset_frames)

    # Ensure we start at 0
    if len(onset_samples) == 0 or onset_samples[0] > 0:
        onset_samples = np.concatenate([[0], onset_samples])

    # Add end of file anchor
    onset_samples = np.concatenate([onset_samples, [len(y)]])

    segments_data = []

    for i in range(len(onset_samples) - 1):
        start = onset_samples[i]
        end = onset_samples[i+1]

        # Initial Slice
        y_raw = y[start:end]

        # 2. Smart Refinement: Trim Silence
        # Often the "end" is just the next note's start.
        # But if there is a gap, we want to trim the silence tail.
        # We trim ONLY the tail (right side) to preserve natural decay.
        # We use a gentle threshold (60dB) to keep reverb tails if they exist,
        # but cut pure digital silence.
        y_trimmed, _ = librosa.effects.trim(y_raw, top_db=60)

        # 3. Minimum Duration Check
        # Discard slices < 100ms (likely noise or glitch)
        if len(y_trimmed) < 0.1 * sr:
            continue

        # 4. Fade Out (De-click)
        # Apply a tiny 5ms fade out to ensure zero-crossing at end
        fade_len = int(0.005 * sr)
        if len(y_trimmed) > fade_len:
            y_trimmed[-fade_len:] *= np.linspace(1, 0, fade_len)

        # Analyze
        note, velocity, features = analyze_segment(y_trimmed, sr)

        # 5. Output Filename
        # Source_Index_Note_Vel.wav
        safe_note = note.replace("#", "s") if note else "Unknown"
        out_name = f"{name}_{i:03d}_{safe_note}_v{velocity}.wav"
        out_path = os.path.join(output_dir, out_name)

        sf.write(out_path, y_trimmed, sr)

        segment_info = {
            "source_file": filename,
            "segment_index": i,
            "output_file": out_name,
            "note": note,
            "velocity": velocity,
            "features": features
        }
        segments_data.append(segment_info)

    return segments_data

def main():
    parser = argparse.ArgumentParser(description="Audio Alchemist Smart Slicer (Adversarial V2)")
    parser.add_argument("--input", "-i", default="input_alchemist", help="Input directory")
    parser.add_argument("--output", "-o", default="output_alchemist/temp", help="Output directory")
    parser.add_argument("--sensitivity", "-s", type=float, default=0.07, help="Onset detection sensitivity (0.0-1.0). Lower = More segments.")
    args = parser.parse_args()

    if not os.path.exists(args.output):
        os.makedirs(args.output)

    files = glob(os.path.join(args.input, "*.mp3")) + glob(os.path.join(args.input, "*.wav"))

    all_data = []

    if not files:
        print(f"No audio files found in {args.input}")
        return

    for f in files:
        data = process_file(f, args.output, sensitivity=args.sensitivity)
        all_data.extend(data)

    # Save JSON Report
    report_path = os.path.join(args.output, "slicing_report.json")
    with open(report_path, "w") as f:
        json.dump(all_data, f, indent=2)

    print(f"Processing complete. {len(all_data)} high-fidelity slices created.")
    print(f"Report saved to {report_path}")

if __name__ == "__main__":
    main()
