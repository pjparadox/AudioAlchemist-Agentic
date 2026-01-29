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
*   **Mai:** Translate text (Chunking applied). No Em Dashes.
*   **Quang:** Enforce Kinship Graph (Public/Private/Power).
*   **Linh:** Check for "Register Collapse".

### 3. Special Referrals (Cross-Team)
*   **Legal Language:** If text contains legal jargon (contracts/court), refer to **Gavel** with `[REFERRAL: FICTION_WAIVER]`. Integrate their notes.
*   **Poetry/Lyrics:** If text contains song/poem, refer to **Orpheus**. Check for "Prophecy" status.

### 4. Formatting & QC
*   **Sera:** Enforce Timecodes & Format. Suffix must be `-vn.srt`. No Em Dashes.
    *   **Timing Protocol (Netflix Rule):**
        *   **Start Times:** IMMUTABLE.
        *   **End Times:** Flexible (Extend to lower CPS if no overlap).
        *   **Condensation:** If CPS > 20, **REWRITE** to shorten. Voice > Literalism.
*   **Vu:**
    *   **Cross-Division Ping:** Consult Thoth/Maat/Justitia if relevant.
    *   **CPS Audit:** Enforce the Condensation Protocol.
    *   Execute **Adversarial Loop (MQM-Lite)** using `QC_CHECKLIST_MASTER.md`.
    *   If score < 9.8/10, Reject.

## Ambiguity Protocol (Mercury)
*   If context is missing, request **Mercury**.
*   If Mercury fails, **INFER**. Do not stall.
