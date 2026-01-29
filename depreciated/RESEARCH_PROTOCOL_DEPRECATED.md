# SOP: Deep Research Protocol (The Argus Cycle)

**Division:** Argus (Research & Intelligence)
**Owner:** Athena (Supervisor)
**Scope:** All "Deep Dive" research projects intended to support Creative Nonfiction, Historical Fiction, or True Crime adaptation.

## 1. Phase I: Initialization (Varys)
*   **Goal:** Establish the project scope and structure.
*   **Action:**
    1.  Create directory: `context/projects/[Project_Name]/`.
    2.  Create subdirectories:
        *   `primary_docs/` (The "Gold" Layer).
        *   `raw_research/` (Web dumps, broad context).
        *   `reports/` (Synthesized analysis).
    3.  **Checklist Injection:** Ask the user for specific "Research Prompts" or a "Checklist". If missing, proceed with a "Best Effort" standard based on the project type (e.g., Timeline, Persons, Legal).

## 2. Phase II: The Deep Dive (Mercury)
*   **Goal:** Gather "Texture" and "Structure".
*   **Action:** Execute search queries based on the checklist.
*   **Deliverables:**
    *   `FACTS.md`: Objective data points (Dates, Locations, Stats).
    *   `TIMELINE.md`: High-level chronology.
    *   `PROFILES.md`: Dossiers on key players (Psychology, Motive).
    *   `MYTHMAKING.md`: How the story is perceived by the public vs. reality.

## 3. Phase III: The Primary Hunt (Cipher)
*   **Goal:** Secure the "Artifacts".
*   **Action:**
    1.  Search for specific documents: Court verdicts, Autopsy reports, Letters, Diaries, Transcripts.
    2.  **The Dutiful Transcription Protocol:**
        *   If the PDF/Raw file is unavailable, **transcribe** the text from web sources.
        *   Save Original: `primary_docs/[Name].txt`.
        *   Save Translation: `primary_docs/[Name]-English.txt`.
    3.  **Evidence Log:** Update `EVIDENCE_LOG.md` with every item found (or "Missing/Rumored").

## 4. Phase IV: Synthesis & Analysis (Varys/Mercury)
*   **Goal:** Turn data into actionable narrative intelligence.
*   **Deliverables (Saved in `reports/`):**
    *   `SOURCE_MAP.md`: Reliability ranking of all sources.
    *   `FORENSIC_TIMELINE.md`: A day-by-day reconstruction with "Pivot Points".
    *   `MEDICAL_RESEARCH.md` (or Topic Specific): Deep dive into the technical reality (e.g., Physiology, Ballistics, Law).
    *   `DIVERGENCE_LEDGER.md`: Comparison of Reality vs. Fiction/Myth.
    *   `CONVERSION_STRATEGY.md`: Paths for adaptation (e.g., "Creative Nonfiction" vs. "Inspired Fiction").

## 5. Phase V: The Athena Audit (Supervisor)
*   **Goal:** QC the dataset.
*   **Action:** Athena reads all generated files and issues `reports/ATHENA_EVALUATION.md`.
*   **Criteria:**
    *   **Structure:** Are all folders and core files present?
    *   **Texture:** Is there enough sensory detail?
    *   **Integrity:** Are translations marked? Are sources cited?
*   **Verdict:** PASSED / FAILED (with remediation plan).

## 6. Output
The project is considered "Ready for Quill" (Drafting) only when Athena issues a **PASSED** verdict.
