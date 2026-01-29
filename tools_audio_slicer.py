import os
import argparse
import librosa
import numpy as np
import soundfile as sf
import json
from glob import glob

def hz_to_note_name(hz):
    if hz is None or hz <= 0:
        return "Unknown"
    return librosa.hz_to_note(hz)

def amplitude_to_velocity(amp):
    # Map 0.0-1.0 to 0-127
    return int(np.clip(amp * 127, 0, 127))

def analyze_segment(y, sr):
    # Pitch detection
    f0, voiced_flag, voiced_probs = librosa.pyin(y, fmin=librosa.note_to_hz('C1'), fmax=librosa.note_to_hz('C8'), sr=sr)
    if f0 is not None:
        avg_f0 = np.nanmedian(f0)
        if np.isnan(avg_f0):
            note = "Unknown"
        else:
            note = hz_to_note_name(avg_f0)
    else:
        note = "Unknown"

    # Velocity (Peak Amplitude)
    peak_amp = np.max(np.abs(y))
    velocity = amplitude_to_velocity(peak_amp)

    # Features for Description
    centroid = np.mean(librosa.feature.spectral_centroid(y=y, sr=sr))
    rolloff = np.mean(librosa.feature.spectral_rolloff(y=y, sr=sr))
    zcr = np.mean(librosa.feature.zero_crossing_rate(y))

    features = {
        "spectral_centroid": float(centroid),
        "spectral_rolloff": float(rolloff),
        "zero_crossing_rate": float(zcr),
        "duration": float(len(y) / sr)
    }

    return note, velocity, features

def process_file(filepath, output_dir):
    filename = os.path.basename(filepath)
    name, ext = os.path.splitext(filename)

    print(f"Processing: {filename}")
    try:
        y, sr = librosa.load(filepath, sr=None)
    except Exception as e:
        print(f"Error loading {filename}: {e}")
        return []

    # Detect onsets
    onset_frames = librosa.onset.onset_detect(y=y, sr=sr, backtrack=True)
    onset_samples = librosa.frames_to_samples(onset_frames)

    # Add end of file
    onset_samples = np.concatenate([onset_samples, [len(y)]])

    segments_data = []

    for i in range(len(onset_samples) - 1):
        start = onset_samples[i]
        end = onset_samples[i+1]

        # Skip very short segments (< 0.1s)
        if (end - start) < 0.1 * sr:
            continue

        y_segment = y[start:end]

        # Apply fade out to avoid clicks
        fade_len = int(0.01 * sr)
        if len(y_segment) > fade_len:
            y_segment[-fade_len:] *= np.linspace(1, 0, fade_len)

        # Analyze
        note, velocity, features = analyze_segment(y_segment, sr)

        # Output Filename: Source_Index_Note_Vel.wav
        # We use a temporary naming convention. Euterpe will finalize it.
        # Clean note name for filename (remove #)
        safe_note = note.replace("#", "s") if note else "Unknown"
        out_name = f"{name}_{i:03d}_{safe_note}_v{velocity}.wav"
        out_path = os.path.join(output_dir, out_name)

        sf.write(out_path, y_segment, sr)

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
    parser = argparse.ArgumentParser(description="Audio Alchemist Slicer Tool")
    parser.add_argument("--input", "-i", default="input_alchemist", help="Input directory")
    parser.add_argument("--output", "-o", default="output_alchemist/temp", help="Output directory")
    args = parser.parse_args()

    if not os.path.exists(args.output):
        os.makedirs(args.output)

    files = glob(os.path.join(args.input, "*.mp3")) + glob(os.path.join(args.input, "*.wav"))

    all_data = []

    if not files:
        print(f"No audio files found in {args.input}")
        return

    for f in files:
        data = process_file(f, args.output)
        all_data.extend(data)

    # Save JSON Report
    report_path = os.path.join(args.output, "slicing_report.json")
    with open(report_path, "w") as f:
        json.dump(all_data, f, indent=2)

    print(f"Processing complete. {len(all_data)} slices created.")
    print(f"Report saved to {report_path}")

if __name__ == "__main__":
    main()
