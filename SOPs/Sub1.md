# SOP: SubTeam6 (Subtitles) — THE GOLDEN PROMPT

MISSION: Translate + QA ONE episode using Sub Team Six workflow.
OUTPUT LANGUAGE: [Target_Language] (Default: vi)

## Paths
- **SOURCE:** `/input_subs/[Filename].srt`
- **OUTPUT:** `/output_subs/[Filename]-[Lang].srt`
- **CONTEXT (Required):**
    - `/foundation/` (Protocols & Roster)
    - `/Context/projects/{Current_Project}/*` (All files)
    - `/Context/Linguistics/{Target_Language}/*`

## Non-negotiable rules
1. **Do not change any start times** from the original SRT.
2. You may extend **end times only** if there is **no overlap**.
3. Use the `MASTER_KINSHIP_MAP` and `CONTEXT_BEATS` as the absolute Source of Truth for pronouns/register.
4. Produce subtitles optimized for **low vision** (large font; comfort-first).

## Ad / Watermark removal policy (IMPORTANT)
- Remove subtitle-team artifacts (URLs, Discord, "sub by...").
- **Do NOT remove** story content (e.g., "[TV AD PLAYING]" if part of the scene).

## Readability / comfort targets
- **Prefer ≤ 16 CPS.**
- Flag 16–20 CPS.
- **Critical > 23 CPS:** Fix by extending end time (no overlap) or condensing text.

## Chunking protocol (Default 200 cues, max 300)
1. Process in chunks of **200 cues**.
2. If stalling, drop to **100 cues**.
3. **Save output after every chunk.**
4. **Context Loop:**
   - BEFORE processing: Read `PROGRESS_LOG.md` for context.
   - AFTER processing: Update `PROGRESS_LOG.md` with a summary of the plot events in this chunk.

## Stop-everything anti-stall rule
If you write more than 1 paragraph of planning without producing output:
- **STOP immediately.**
- Switch to 100-cue chunks.
- Complete the next chunk and write it to disk.

**START NOW.**
1. Run **Cupid** (if script exists).
2. Begin **Chunk 1**.