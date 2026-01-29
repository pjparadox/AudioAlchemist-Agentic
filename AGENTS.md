# Interpretor Agent Suite — Agent Directory
*(Formerly Sub Team Six)*

This repository contains the **Recursive Modular Orchestrator**, a multi-agent workflow for subtitle transcription, translation, and quality assurance, governed by **Kinship-Graph** principles.

## Directory Structure

### `/Agents/`
Individual agent instructions.
*   `/Agents/SubTeam6/`: Subtitle Specialists.
*   `/Agents/Quill/`: Fiction/Literary Specialists.
*   `/Agents/Core/`: Core Utilities.
*   `/Agents/Scholar/`: Academic/Pedagogical Specialists.
*   `/Agents/AudioAlchemist/`: Audio Analysis Specialists.

### `/input_subs/`
Original-language subtitle files (SRT).
These are the source-of-truth timings. Start times must not be changed.

### `/output_subs/`
Latest “best” translated subtitle files.
Output files must use a **hyphen suffix** for language, e.g.:
*   `S02E04-vn.srt` (Correct)
*   `S02E04.vn.srt` (Incorrect)

### `/output_subs/old/`
Archived previous versions.
When revisions are made, move the previous “best” file here before saving a new one.

### `/context/`
Reference materials: kinship maps, plot beats, language notes, character personalities.
*   **Templates:** `/context/templates/KINSHIP_GRAPH_SCHEMA.md`

### `/input_av/` (optional / future)
Audio/video inputs that may be transcribed into `/input_subs/`.

## Recursive Modular Orchestrator (Pipeline)

*   **Mai** — Lexical Generator (Accuracy-First, Political-Blind)
*   **Quang** — Kinship & Status Adjudicator (Queries Kinship Graph)
*   **Linh** — Context Anthropologist (Voice, Register, Mode Switching)
*   **Noah** — Cultural Bridge Auditor (Transferable Value)
*   **Cato** — CPS Metrician (Automated Hotspot Finder)
*   **Nemesis** — Relational Shift Detector (Status Changes)
*   **Vu** — Supervisor / Final QC (Readability + CPS Strictness)

## Optional Support Agents & Specialized Divisions

### Fiction Division (Quill)
*   **Lyra** — Literary Stylist (Prose & Flow)
*   **Elara** — Voice & Culture Harmonizer (Ghost Writer)
*   **Orpheus** — Lyricist & Poet (Song Adaptation)
*   **Thoth** — Literary Editor / QC (Narrative Force & Market Readiness)
*   **Proteus** — Style Analyst & Mimic (The Shapeshifter)
*   **Huy** — Local Consumer Reviewer (Native Reader Simulation)

### Hephaestus (Manuscript Revision & Reforging)
*   **The Forge Master** — Revision Supervisor & QC (Pipeline Manager)
*   **Calliope** — Developmental Editor (Structure & Pacing)
*   **Vulcan** — Line Editor & Stylist (Prose Polish & Em Dash Hunter)
*   **Echo** — Voice Preservationist (Guardian of Author's Soul)
*   **Gutenberg** — Publishing Format Auditor (Formatting, Output Verification)

### The Muse (Developmental Editing Division)
*   **The Architect** — Structural Engineer. Focuses on plot holes, narrative arcs, and causality. Ensures the "bones" of the story are solid.
*   **The Psych** — Character Psychologist. Focuses on motivation, agency, emotional resonance, and consistency. Ensures characters are not "damp saltines."
*   **The Pacer** — Flow Analyst. Focuses on tension, scene length, and engagement. Prevents the "soggy middle."
*   **The Market** — Bestseller Analyst. Focuses on genre expectations, hooks, and marketability. Asks: "Would this sell?"

### Gavel (Legal Division)
*   **Themis** — Legal Translator (Equivalence & Disclaimer Protocol)
*   **Themis (Auditor)** — Legal Obligation & Role Auditor (Procedural Hardening)
*   **Forseti** — Legal Analyst (Context Interpretation & Implications)
*   **Justitia** — Legal QC (Accuracy & Safety Enforcer)

### Caduceus (Medical Division)
*   **Asclepius** — Medical Translator (Doctor-to-Doctor / Clinical Precision)
*   **Panacea** — Patient Liaison (Doctor-to-Patient / Cognitive Ramp)
*   **Qyburn** — Medical QC (Disgraced Maester / Safety & Dosage Check)

### Argus (Research & Intelligence)
*   **Athena** — Research Supervisor & QC (The All-Seeing Eye)
*   **Cipher** — Forensic Philologist (Primary Source & Transcription)
*   **Varys** — Research Director (Strategy & Checklist)
*   **Mercury** — Context Gap Hunter (Deep Dive Research)

### Oversight (Internal Affairs & Governance)
*   **The Architect** — Chief Governance Officer & System Auditor (Protocol Authority). **Special Directive:** Enforce Consolidated Logging Protocol.
*   **The Sentry** — Compliance Officer (Diff Inspection & Log Enforcement)

### Core & Scholar
*   **Atlas** — Reverse Translator (Input → English)
*   **Sophia** — Academic Pedagogy (Scaffolding & Cognitive Ramp)
*   **Maat** — Academic QC (Truth, Rigor & Pedagogical Accuracy)
*   **Mercury** — Context Gap Hunter (Research & Feedback Integration)
*   **Varys** — Research Director (QC & Knowledge Supervisor)
*   **Palinurus** — Regression Sentinel (Diff vs Prior Best)
*   **Mercator** — Named Entity Verifier (Audit Trail)
*   **Eris** — Adversarial Red-Teamer (Hallucination/Tone)
*   **Janus** — Change Log Guardian (Version Control & Deprecation)

### Utilities
*   **Tuan** — Transcriptionist (A/V → SRT + Evidence Normalization)
*   **Cupid** — Speaker Identification Matchmaker (State Hypotheses)
*   **Sera** — Constitutional Layer (Format, Timestamps)
*   **Minh** — Institutional Memory (Terminology/Glossary)
*   **Metatron** — System Archivist (Master Ledger)

### Heart & Home (Emotional Intelligence & Communications)
*   **Athena** — Professional Liaison (Workplace Strategist & Hierarchy Navigator).
*   **Eros** — Romantic Nuance Agent (The Romantic Nuance Specialist).
*   **Hermes** — Culture & Nuance Messenger (Context Note Taker & Cultural Bridge).
*   **Hestia** — Heart Router & Family Liaison (The Sincerity Engine).
*   **Iris** — Instant Messenger (Digital Literacy, Slang, & Emojis).
*   **Philia** — Friendship Liaison (Camaraderie & Casualness).
*   **Psyche** — Tone Shift Detector (Relationship Dynamic Monitor).

### Audio Alchemist (Audio Analysis & Processing)
*   **Apollo** — Audio Director & QC (Output Supervisor).
*   **Pan** — The Slicer (Script Operator & Signal Processor).
*   **Euterpe** — The Sonic Poet (Timbre Description & Metadata).

### The Veil (Specialized Safety & Accessibility)
*   **Lilith** — Trauma Register Guardian (Harm Reduction & Sensitive Context).
*   **Morpheus** — Cognitive Load & Intent Auditor (Mental Energy & Accessibility).

### Grigori (System Integrity & Enforcement)
*   **Ananke** — Constraint Enforcer (The Inevitability Enforcer).
*   **Azrael** — Audit Angel (Final Integrity Verifier & Process Gatekeeper).
*   **Metis** — Drift Oracle (Semantic Drift & Entropy Detector).

### Scribes of Old Valyria (Franchise Specialists)
*   **Maester Vaelor** — Canon Linguist (IP Integrity & Franchise Terms).
*   **Pythia** — Register Oracle (Predictive Register Checker).

## Global Rules

1.  **Do not change start times** from the original subtitle file (Constitutional Law).
2.  You may extend end times if and only if there is no overlap with the next cue.
3.  Remove all advertisements/watermarks from any subtitle file encountered.
4.  Maintain consistent Vietnamese register using **Kinship Graph** references.
5.  If uncertain about names/places/terms, use internet search to confirm.
6.  **NO EM DASHES (—):** Under no circumstances output an Em Dash. Replace with comma, rephrase, or use a hyphen `-`.
7.  **DEPRECATION INTEGRITY:** Files in `depreciated/` must **NEVER** be overwritten or deleted. Always rename with a timestamp (e.g., `_20241027_1200.md`) before moving to deprecation.
8.  **NON-CODING MANDATE:** Agents must **NEVER** use scripts for cognitive tasks (writing, editing, translation, QC). Scripts are permitted **ONLY** for file format conversion, splitting input files, or merging output files. All prose generation and critical thinking must be performed by the agent's LLM core.
9.  **GLOBAL CONTEXT & SOURCE BOUNDARY POLICY:**
    *   **Project Isolation:** Agents must strictly confine their context retrieval to the specific project folder they are working on (e.g., `context/projects/Freehaven_Online/`). Accessing files from unrelated projects (e.g., `Deadpool`, `Emily_Rose`) is strictly prohibited to prevent narrative cross-contamination.
    *   **Source Authority:** The only valid source for narrative content is the file located in the project's specific input directory (e.g., `input_quill/Freehaven Online - Ebook.doc`). Agents must ignore conflicting information from "Story Bibles" or external summaries if they contradict the primary source text.
    *   **Context Granularity:** Agents **MUST** consult specific sub-folders within the project context for detailed information.
        *   `Context/Characters/Major/` & `Context/Characters/Minor/`: Consult individual character files for detailed speech patterns, quotes, and history. **Voice Consistency is Paramount.**
        *   `Context/Locations/`: Individual files for each location.
        *   `Context/Events/`: Files for major plot events.
        *   `Context/Lore/`: Files for Races, Monsters, Magic, Gear, Titles, and Quests.
    *   **Global vs. Local:** General linguistic rules (e.g., Vietnamese grammar, glossary terms in `context/global/`) are universal. However, all plot beats, character names, and stylistic directives must be sourced exclusively from the active project's local context.

## Initialization Mandate
**All sessions must begin by consulting `SESSION_INIT.md` located in the root directory. This document serves as the "First Contact" protocol, outlining critical mandates for non-pruning, log consolidation, and operational hygiene.**
