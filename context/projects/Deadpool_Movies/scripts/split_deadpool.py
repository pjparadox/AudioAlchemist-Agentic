import re
import os

def parse_srt(content):
    pattern = r'(\d+)\n(\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3})\n((?:.|\n)*?)(?=\n\n|\Z)'
    matches = re.findall(pattern, content)
    # Fallback if regex fails (simple block split)
    if len(matches) < 10:
        print("Regex failed, using block split fallback")
        matches = []
        blocks = content.strip().split('\n\n')
        for block in blocks:
            lines = block.split('\n')
            if len(lines) >= 3:
                # index is lines[0], time is lines[1], text is the rest
                matches.append((lines[0], lines[1], '\n'.join(lines[2:])))
    return matches

def split_srt():
    input_path = "input_subs/Deadpool 2 Super Duper Cut UNRATED (2018) 1080p (Resync).srt"
    output_dir = "context/projects/Deadpool_Movies/working_subs/"

    with open(input_path, 'r', encoding='utf-8-sig') as f:
        content = f.read().replace('\r\n', '\n')

    cues = parse_srt(content)
    print(f"Total cues found: {len(cues)}")

    ranges = [
        (1, 250),
        (251, 500),
        (501, 750),
        (751, 1000),
        (1001, 1250),
        (1251, 1500),
        (1501, 1750),
        (1751, 2000),
        (2001, 3000) # Catch all till end
    ]

    for i, (start, end) in enumerate(ranges):
        chunk_cues = []
        for index, time, text in cues:
            idx = int(index)
            if idx >= start and idx <= end:
                chunk_cues.append(f"{index}\n{time}\n{text}\n")

        chunk_filename = f"chunk_{i+1}.srt"
        output_path = os.path.join(output_dir, chunk_filename)

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(chunk_cues))

        print(f"Created {chunk_filename} with {len(chunk_cues)} cues.")

if __name__ == "__main__":
    split_srt()
