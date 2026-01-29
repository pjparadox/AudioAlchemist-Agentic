# Standard Operating Procedure: Subtitle Translation (Interpretor Suite)

## Purpose
To produce high-fidelity, kinship-aware Vietnamese subtitles (`.vn.srt`) for high-context narrative media.

## Agents Involved
*   **Tuan/Cupid:** Transcription & Identity.
*   **Mai:** Lexical Draft.
*   **Quang:** Kinship Adjudication.
*   **Linh:** Context/Voice.
*   **Sera:** Format.
*   **Vu:** QC & Adversarial Loop.

## Workflow

### 1. Pre-Processing
*   Input SRT → `input_subs/`.
*   Run **Cupid** to tag speakers (if script available).

### 2. Translation & Adjudication
*   **Mai:** Translate text (Chunking applied).
*   **Quang:** Enforce Kinship Graph (Public/Private/Power).
*   **Linh:** Check for "Register Collapse".

### 3. Formatting & QC
*   **Sera:** Enforce Timecodes & Format. Suffix must be `.vn.srt`.
*   **Vu:**
    *   Check CPS (≤16 Ideal).
    *   Execute **Adversarial Loop (8 Degrees)**.
    *   If score < 9.8/10, Reject.

## Ambiguity Protocol (Mercury)
*   If context is missing, request **Mercury**.
*   If Mercury fails, **INFER**. Do not stall.
