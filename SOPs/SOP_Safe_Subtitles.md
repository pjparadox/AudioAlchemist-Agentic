# SOP: Safe Subtitles (Lilith Integration)

## Purpose
To produce subtitles that include specific Content Warnings (CW) for trauma/triggers without altering the original timeline or content.

## Agents Involved
*   **SubTeam6 Pipeline:** (Tuan -> Cupid -> Mai -> Quang -> Linh -> Sera -> Vu).
*   **Lilith:** (Mode 1: Sentinel).

## Workflow

### 1. Standard Processing
Run standard **SubTeam6** pipeline to generate `[filename]-vn.srt`.

### 2. Lilith Scan
**Lilith** reads the *finished* translation.
*   **Scan:** Look for triggers (Sexual Violence, Self-Harm, Domestic Abuse, Extreme Gore).
*   **Verdict:**
    *   *None Found:* No action.
    *   *Found:* Generate specific warning text (e.g., "CW: Self-Harm").

### 3. Splash Insertion
If triggers are found:
1.  **Check Timing:** Look at Cue 1 Start Time.
2.  **Insert:**
    *   *If Gap exists (00:00 to Cue 1):* Insert new Cue 1 at 00:00:00. Shift indices (Cue 1 -> Cue 2).
    *   *If No Gap:* **DO NOT** shift times. Append warning to the filename (e.g., `[filename]-vn-CW.srt`) and add a text note in `PROGRESS_LOG.md`.

### 4. QC
**Vu** verifies the inserted cue matches the file format.
