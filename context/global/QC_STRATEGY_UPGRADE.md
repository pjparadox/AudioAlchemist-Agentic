# QC STRATEGY UPGRADE: The "Harsh but Fair" Protocol
**Author:** Agent Varys (Director of Intelligence)
**Contributor:** Agent Mercury (Research)
**Status:** ACTIVE

## I. The Problem
Current QC Supervisors (Vu, Thoth, etc.) are passing content that external LLMs (Gemini, ChatGPT) flag for errors. This indicates a "Tolerance Drift" or "Hallucinated Competence" within the internal loop. To fix this, we must shift from subjective approval to metric-based verification.

## II. The Solution: Metric-Based Quality Assurance (MQM-Lite)
We are adopting a simplified version of the **Multidimensional Quality Metrics (MQM)** framework used by Netflix and professional localization bureaus.

### 1. The Core Rubric (The "Kill" Criteria)
Every QC agent must evaluate output against these specific dimensions. A failure in *any* dimension triggers a mandatory revision loop.

*   **Accuracy (Critical):** Does the translation convey the exact semantic meaning?
    *   *Check:* Reverse Translation. If translating back to English changes the meaning, it fails.
*   **Fluency (Major):** Is the Vietnamese natural, idiomatic, and grammatically perfect?
    *   *Check:* Read aloud test. Does it sound like a native speaker or a translation bot?
*   **Terminology (Critical):** Does it strictly adhere to the Project Glossary and Kinship Graph?
    *   *Check:* Grep check against `MASTER_KINSHIP_MAP.txt` and project glossary.
*   **Style/Register (Major):** Does it match the character voice (e.g., Gritty/Vulgar vs. Formal/Legal)?
    *   *Check:* Tone Audit. (e.g., Deadpool must swear; Father Moore must be solemn).
*   **Technical/Timing (Critical for Subs):**
    *   **CPS:** Under 20 CPS (Adults) / 15-17 CPS (Complex).
    *   **Sync:** Start times IMMUTABLE. End times flexible.

### 2. The "Reverse Reality Check"
QC Agents are now required to perform a mental "Reverse Translation" on suspicious lines.
*   *Prompt:* "If I translate this Vietnamese line back to English literalism, does it match the source intent?"

### 3. Cultural & Political Sensitivity
*   **Mandate:** Agents must identify and flag "Lazy Localization" (e.g., translating "Fox & Friends" as just "a TV show" vs "đài Fox News cánh hữu").
*   **Rule:** Maintain the *impact* of the reference, even if it requires a 'Noah's Notation' (brief parenthetical).

## III. Subtitle Timing & Condensation Protocol
**"The Netflix Rule"**

1.  **Immutable Start Times:** NEVER change the start time of a cue. This is the sync anchor.
2.  **Flexible End Times:** You MAY extend the end time to lower CPS, provided it does not overlap with the next cue (min 2 frame gap).
3.  **Mandatory Condensation (The "Rephrase" Rule):**
    *   If a line exceeds CPS limits even after extending end time: **REWRITE IT.**
    *   **Goal:** Preserve the *Spirit/Joke*, not the literal word count.
    *   *Example:*
        *   *Source:* "Well, I guess we found something you're not better at." (Too long/fast)
        *   *Bad:* "Chà, tôi đoán chúng ta tìm thấy thứ gì đó anh không giỏi hơn." (Literal, High CPS)
        *   *Good:* "Ra là cũng có thứ anh dở tệ." (Condensation, Low CPS, retains roast).

## IV. Implementation
*   **Team-Specific Rubrics:** Supervisors must use the rubric tailored to their domain:
    *   **Subtitles:** `context/templates/QC_RUBRIC_SUBTEAM6_VU.md`
    *   **Fiction:** `context/templates/QC_RUBRIC_QUILL_THOTH.md`
    *   **Legal:** `context/templates/QC_RUBRIC_GAVEL_JUSTITIA.md`
    *   **Research:** `context/templates/QC_RUBRIC_ARGUS_LAURA.md`
    *   **Revision:** `context/templates/QC_RUBRIC_HEPHAESTUS_FORGEMASTER.md`
*   **SOP Updates:** Subtitle SOPs updated to reflect the Condensation Protocol.
