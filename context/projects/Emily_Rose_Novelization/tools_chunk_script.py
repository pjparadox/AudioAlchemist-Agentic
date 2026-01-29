import os
import re

def chunk_script(source_path, output_dir, chunk_size=1000):
    with open(source_path, 'r', encoding='utf-8') as f:
        text = f.read()

    # Split by scene headers (INT. or EXT.) to respect scene boundaries
    # But first, let's normalize newlines
    lines = text.split('\n')

    chunks = []
    current_chunk = []
    current_word_count = 0

    for line in lines:
        words = len(line.split())

        # Check if we are at a scene boundary AND we have enough words
        # Or if we just have way too many words
        is_scene_header = line.strip().startswith('INT.') or line.strip().startswith('EXT.')

        if (current_word_count >= chunk_size and is_scene_header) or (current_word_count > chunk_size * 1.5):
            chunks.append('\n'.join(current_chunk))
            current_chunk = []
            current_word_count = 0

        current_chunk.append(line)
        current_word_count += words

    if current_chunk:
        chunks.append('\n'.join(current_chunk))

    for i, chunk in enumerate(chunks):
        filename = f"chunk_{i+1:02d}.txt"
        with open(os.path.join(output_dir, filename), 'w', encoding='utf-8') as out:
            out.write(chunk)

    print(f"Created {len(chunks)} chunks.")

if __name__ == "__main__":
    chunk_script(
        "context/projects/Emily_Rose_Novelization/input_quill/source_script.txt",
        "context/projects/Emily_Rose_Novelization/input_quill/chunks/"
    )
