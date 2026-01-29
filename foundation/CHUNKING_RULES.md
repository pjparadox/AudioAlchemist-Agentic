# Chunking Rules (Non-negotiable)

## PART 1: SUBTITLES (Time-Based)
**Work Unit:** Cues (Lines).

### Core Rule
Work in fixed chunks and commit output after each chunk. Reference previous chunk summary before beginning to bring immediate context up to speed.

### Chunk Size
*   **Default:** 200 cues per chunk.
*   **If Stalling Occurs:** Drop to 50 cues per chunk.
*   **Hard Limit:** Never exceed 300 cues per chunk.

### Progress Bookkeeping (Required after every chunk)
After completing each chunk, write a progress log entry containing:
*   Episode/File Name
*   Chunk Number
*   Cue Range (e.g., 1–50)
*   Last Cue Processed (Number + Timestamp)
*   Output Persistence: Save the current work to `/output_subs/`.
*   Log Update: Append this status to `/context/PROGRESS_LOG.md`.

### Anti-Stall Watchdog
If you produce >2 paragraphs of text without naming the current chunk or writing output to disk, you must STOP and resume with: "RESUME CHUNK N: cues X–Y".
If you detect looping/apologizing, immediately switch to 25-cue chunks.

### Constraints (The Netflix Rule)
*   **Start Times:** IMMUTABLE. Never change.
*   **End Times:** Flexible. Extend to lower CPS if no overlap (min 2-frame gap).
*   **Condensation:** If CPS > 20, **REPHRASE** to shorten. Do not just translate literally. Voice > Word Count.

## PART 2: MANUSCRIPTS (Text-Based)
**Applicability:** Fiction (Quill), Academic (Scholar), Legal (Gavel).
**Work Unit:** Words (rounded to nearest Paragraph).
- **Default Chunk:** ~2,000 words.
- **Constraint:** NEVER split a paragraph. Always finish the paragraph before ending the chunk.
- **Procedure:**
    1.  **Process:** Translate/Analyze the 2,000-word chunk.
    2.  **Summary Chain:** After Chunk 1, create a **Master Context Note**. For all subsequent chunks, READ this note first to establish context.
    3.  **Update:** After finishing a chunk, append new plot/term/context developments to the Master Context Note.
    4.  **Save:** Save chunk as a standalone file (e.g., `Chapter1_Part1.md`).

## PART 3: MERGE PROTOCOL (Manuscripts)
1.  **Chunk Assembly:** Merge `Part1`, `Part2`, etc., into `Chapter_X.md`.
2.  **Manuscript Assembly:** Merge all Chapters into `Full_Manuscript.md`.
3.  **Front Matter Check:** QC must verify Title, Dedication, Copyright, etc.
4.  **Blurb Protocol:** If missing, generate a sales-optimized blurb (Target Score: 9.9/10).

## GLOBAL ANTI-STALL RULE
If you produce >2 paragraphs of "planning" without outputting the translated chunk:
1. **STOP** immediately.
2. Reduce chunk size by 50%.
3. Resume processing.
