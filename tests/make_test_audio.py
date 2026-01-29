import numpy as np
import soundfile as sf
import os
import librosa

def generate_sine_wave(freq, duration, sr=22050):
    t = np.linspace(0, duration, int(sr * duration), endpoint=False)
    return 0.5 * np.sin(2 * np.pi * freq * t)

def create_test_audio():
    sr = 22050
    # Create 3 notes: C4 (261.63), E4 (329.63), G4 (392.00)
    # 0.5s note, 0.5s silence
    note1 = generate_sine_wave(261.63, 0.5, sr)
    silence = np.zeros(int(sr * 0.5))
    note2 = generate_sine_wave(329.63, 0.5, sr)
    note3 = generate_sine_wave(392.00, 0.5, sr)

    # Concatenate: Note1 - Silence - Note2 - Silence - Note3
    y = np.concatenate([note1, silence, note2, silence, note3])

    # Ensure input directory exists
    if not os.path.exists("input_alchemist"):
        os.makedirs("input_alchemist")

    sf.write("input_alchemist/test_sine_arpeggio.wav", y, sr)
    print("Created input_alchemist/test_sine_arpeggio.wav")

if __name__ == "__main__":
    create_test_audio()
