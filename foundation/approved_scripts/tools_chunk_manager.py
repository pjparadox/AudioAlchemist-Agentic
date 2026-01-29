import re
import os
import sys

def parse_srt(content):
    cues = []
    # Regex to capture: Index, Time, Text
    # Handles potential multi-line text
    # \d+\s+ -> Index
    # \d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}\s+ -> Time
    # (.*?)(?=\n\d+\s+\d{2}:\d{2}:\d{2},\d{3}|\Z) -> Text (up to next cue or EOF)

    # Simpler approach: Split by double newlines, but SRTs can be messy.
    # Let's use the regex from the trace 1349 cues

    pattern = r'(\d+)\n(\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3})\n((?:.|\n)*?)(?=\n\n|\Z)'
    matches = re.findall(pattern, content)

    # If regex misses due to messy format, fall back to block splitting
    if len(matches) < 10:
        blocks = content.strip().split('\n\n')
        for block in blocks:
            lines = block.split('\n')
            if len(lines) >= 3:
                cues.append((lines[0], lines[1], '\n'.join(lines[2:])))
        return cues

    return matches

def extract_chunk(input_path, output_path, start_index, end_index):
    try:
        with open(input_path, 'r', encoding='utf-8-sig') as f:
            content = f.read()
            # Normalize line endings
            content = content.replace('\r\n', '\n')

        cues = parse_srt(content)

        # Filter cues based on index
        selected_cues = []
        for index, time, text in cues:
            if int(index) >= start_index and int(index) <= end_index:
                selected_cues.append(f"{index}\n{time}\n{text}\n")

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(selected_cues))

        print(f"Extracted {len(selected_cues)} cues to {output_path}")

    except Exception as e:
        print(f"Error: {e}")

def merge_chunks(chunk_dir, output_path):
    chunks = sorted([f for f in os.listdir(chunk_dir) if f.startswith("chunk_") and f.endswith(".srt")], key=lambda x: int(x.split('_')[1].split('.')[0]))

    all_content = []
    for chunk in chunks:
        with open(os.path.join(chunk_dir, chunk), 'r', encoding='utf-8') as f:
            all_content.append(f.read().strip())

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n\n'.join(all_content))

    print(f"Merged {len(chunks)} chunks to {output_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python tools_chunk_manager.py [extract|merge] ...")
        sys.exit(1)

    action = sys.argv[1]

    if action == "extract":
        # python tools_chunk_manager.py extract input.srt output.srt start end
        extract_chunk(sys.argv[2], sys.argv[3], int(sys.argv[4]), int(sys.argv[5]))
    elif action == "merge":
        # python tools_chunk_manager.py merge chunk_dir output.srt
        merge_chunks(sys.argv[2], sys.argv[3])
