import os

def merge_chunks():
    chunk_dir = "context/projects/Deadpool_Movies/working_subs/"
    output_path = "output_subs/Deadpool 2 Super Duper Cut UNRATED (2018) 1080p (Resync)-vn.srt"

    # Ensure output dir exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    chunks = sorted([f for f in os.listdir(chunk_dir) if f.startswith("chunk_") and f.endswith("_vn.srt")], key=lambda x: int(x.split('_')[1]))

    all_content = []
    for chunk in chunks:
        with open(os.path.join(chunk_dir, chunk), 'r', encoding='utf-8') as f:
            all_content.append(f.read().strip())

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n\n'.join(all_content))

    print(f"Merged {len(chunks)} chunks to {output_path}")

if __name__ == "__main__":
    merge_chunks()
