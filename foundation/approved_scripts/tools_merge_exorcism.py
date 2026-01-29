import os
import re

# --- CONFIGURATION ---
BASE_DIR = os.getcwd()
INPUT_SUBS_DIR = os.path.join(BASE_DIR, "input_subs")

# Input Filenames (Must exist inside 'input_subs')
FILE_FOREIGN = os.path.join(INPUT_SUBS_DIR, "The Exorcism of Emily Rose_(2005)_[eng_Foreign_Parts_23_976_fps].srt")
FILE_ENGLISH = os.path.join(INPUT_SUBS_DIR, "dmd-exorcismer_eng.srt")

# Output Filename
OUTPUT_FILE = os.path.join(INPUT_SUBS_DIR, "The_Exorcism_of_Emily_Rose_MERGED_NoSync.srt")

def parse_srt(filepath, origin_tag):
    """Parses SRT into a list of dicts."""
    cues = []
    if not os.path.exists(filepath):
        print(f"MISSING FILE: {filepath}")
        return []

    content = ""
    for enc in ['utf-8', 'utf-8-sig', 'cp1252']:
        try:
            with open(filepath, 'r', encoding=enc) as f:
                content = f.read()
            break
        except UnicodeDecodeError: continue

    # Regex to capture cues
    pattern = re.compile(r'\d+\s+(\d{2}:\d{2}:\d{2},\d{3})\s-->\s(\d{2}:\d{2}:\d{2},\d{3})\s+(.+?)(?=\n\n|\n\d+\s+\d{2}:\d{2}|\Z)', re.DOTALL)
    
    matches = pattern.findall(content)
    for m in matches:
        start_ms = timestamp_to_ms(m[0])
        end_ms = timestamp_to_ms(m[1])
        text = m[2].strip()
        
        # Colorize foreign text immediately
        if origin_tag == "FOREIGN":
            clean_text = text.replace('<i>', '').replace('</i>', '')
            text = f'<font color="#ffff00">{clean_text}</font>'
            
        cues.append({
            'start': start_ms, 
            'end': end_ms, 
            'text': text,
            'origin': origin_tag
        })
    return cues

def timestamp_to_ms(ts):
    h, m, s_part = ts.split(':')
    s, ms = s_part.split(',')
    return (int(h) * 3600000) + (int(m) * 60000) + (int(s) * 1000) + int(ms)

def ms_to_timestamp(ms):
    if ms < 0: ms = 0
    h, r = divmod(ms, 3600000)
    m, r = divmod(r, 60000)
    s, ms = divmod(r, 1000)
    return "{:02d}:{:02d}:{:02d},{:03d}".format(int(h), int(m), int(s), int(ms))

def merge_and_sort(list_a, list_b):
    """Combines two lists, sorts by time, and merges overlaps."""
    # 1. Combine
    combined = list_a + list_b
    
    # 2. Sort by Start Time
    combined.sort(key=lambda x: x['start'])
    
    # 3. Collapse Overlaps (Optional but cleaner)
    final_list = []
    if not combined: return []
    
    current = combined[0]
    
    for next_cue in combined[1:]:
        # If start times are within 200ms, consider them simultaneous
        if abs(current['start'] - next_cue['start']) < 200:
            # Merge Text
            current['text'] += "\n" + next_cue['text']
            # Extend End Time to the later of the two
            current['end'] = max(current['end'], next_cue['end'])
        else:
            final_list.append(current)
            current = next_cue
    
    final_list.append(current)
    return final_list

def main():
    print("--- EXORCISM MERGE TOOL (NO SYNC) ---")
    
    print("1. Loading Foreign Subs (No Time Shift)...")
    foreign_cues = parse_srt(FILE_FOREIGN, "FOREIGN")
    
    print("2. Loading English Subs...")
    eng_cues = parse_srt(FILE_ENGLISH, "ENGLISH")
    
    print(f"3. Merging {len(foreign_cues)} Foreign + {len(eng_cues)} English cues...")
    merged = merge_and_sort(eng_cues, foreign_cues)
    
    print(f"4. Writing {len(merged)} total cues to {os.path.basename(OUTPUT_FILE)}...")
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        for i, cue in enumerate(merged):
            f.write(f"{i+1}\n")
            f.write(f"{ms_to_timestamp(cue['start'])} --> {ms_to_timestamp(cue['end'])}\n")
            f.write(f"{cue['text']}\n\n")
            
    print("DONE. File merged with original timestamps.")

if __name__ == "__main__":
    main()