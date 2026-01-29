# Interpretor Agent Suite — Processing Protocol
*(Formerly Sub Team Six)*

## Kinship-Graph Governance
This suite operates on the principle of **Kinship-Graph Governance**: adhering to "Relational Clarity" over simple lexical fidelity.
*   **Core Philosophy:** In high-context languages, the "word" is not the fundamental unit of meaning; the "relationship" is.
*   **Mechanism:** External state management (Kinship Graph) enforces register, preventing "Register Collapse."

## Pipeline Order (Recursive Modular Orchestrator)
1.  **Tuan:** (Optional) Transcribes A/V to SRT if no subtitle exists.
2.  **Cupid:** Scans input_subs against screenplays/transcripts to tag [Unknown] speakers.
3.  **Mai:** Lexical Generation (Accuracy-First, Political-Blind).
4.  **Quang:** Kinship & Status Adjudicator (Queries Kinship Graph).
5.  **Linh:** Context & Voice Anthropologist (Public/Private/Humiliation).
6.  **Quill:** Literary Stylist (Flow, Idiom, Prose).
7.  **Noah:** Cultural Bridge (Modern Notes, Transferable Value).
8.  **Minh:** Institutional Memory (Terminology/Glossary).
9.  **Sera:** Constitutional Layer (Timestamps, Format).
10. **Vu:** FINAL BOSS. QC, Readability (CPS), Logic Check.

## Data Flow
*   **Inputs:** `/input_subs/` (Source of Truth)
*   **Outputs:** `/output_subs/[filename]-vn.srt` (Must use Hyphen `-vn`, `-viet`, or `-vietnamese`. NOT `.vi` or `.vn`).
*   **Context:** `/context/` (Source of Truth for Beats, Kinship, Glossary)
*   **Archive:** Move outdated drafts to `/output_subs/old/`

## System Maintenance & Version Control (Janus Protocol)
Whenever a "Working File" (Agent, SOP, Protocol) is modified:
1.  **Engage Janus:**
    *   **Backup:** Copy original to `/depreciated/`.
    *   **Log:** Update `CHANGELOG.md`.
2.  **Update Archive:** Run **Metatron** to regenerate `MASTER_SUITE_ARCHIVE.txt`.

## Tiered Accessibility Standard
This suite enforces specific standards based on content stakes:
*   **Tier 1 (Casual):** Standard translation.
*   **Tier 2 (Narrative/Cultural):** Graph-aware systems required to preserve "Relational Clarity" (e.g., *House of the Dragon*).
*   **Tier 3 (Civic/Legal/Medical):** Mandatory "Kinship Governance" and Human-in-the-Loop auditing.

## Default Task
Translate and QA subtitle files using the agent pipeline, enforcing **Tier 2** standards by default for narrative content.

### Pipeline Detailed Steps
*   **Mai** produces a raw lexical draft (blind to deep politics).
*   **Quang** adjudicates relationships using the **Kinship Graph**.
*   **Linh** prevents "register collapse" by detecting scene mode (Public vs. Private).
*   **Vu** performs final QC with strict **CPS constraints** and **Adversarial Loop**:
    *   **Ideal:** ≤16 CPS
    *   **Caution:** 16–20 CPS
    *   **Critical:** >23 CPS (Must revise)

## Non-negotiables
*   Start times are **immutable** (Constitutional Law).
*   No overlaps.
*   No ads/watermarks.
*   **NO EM DASHES (—):** Replace with comma or hyphen `-`.
*   Use context files (`Kinship Graph`) as source of truth.

---

## Chunking & Anti-Stall Protocol (MANDATORY)

### Why this exists
Large SRTs can cause slowdowns, looping, or partial completion. This protocol forces forward progress.

### Core Rule
Work in fixed chunks and commit output after each chunk. Reference previous chunk summary before beginning to bring immediate context up to speed.

### Chunk size
*   **Default:** 200 cues per chunk
*   **If the model stalls or slows:** drop to 50 cues per chunk
*   **Hard Limit:** Never exceed 300 cues per chunk

### Progress bookkeeping (required after every chunk)
After completing each chunk, write a progress log entry containing:
*   episode/file name
*   chunk number
*   cue range (e.g., 1–50)
*   last cue processed (number + timestamp)
*   what was written/updated (output file path)
*   any issues flagged for later agents
*   detailed summary of content of chunks that have been processed so far for episode (append this until episode is finished)

### Output persistence (required)
After each chunk:
1.  Save the current translated/edited SRT to the target file in `/output_subs/`
2.  Update (append) `/context/PROGRESS_LOG.md`
3.  Clear working memory of the cue text and load the next chunk

### Anti-stall watchdog
If you produce >2 paragraphs without:
1.  naming the current chunk, AND
2.  stating the cue range you’re working on, AND
3.  writing output to disk,
then you must stop and resume with:
`“RESUME CHUNK N: cues X–Y”`

### “Stop Everything” override
If you detect stalling (repeating, apologizing, summarizing, or proposing plans without edits):
*   Immediately switch to 25-cue chunks
*   Complete the next chunk before writing any additional commentary

### Verification loop per chunk (lightweight, fast)
For each chunk:
1.  Load corresponding cue range from original + candidate translation
2.  Apply rules from `/context/*`
3.  Run: ad/watermark scan, overlap check, and CPS hotspot check
4.  Apply fixes
5.  Save
