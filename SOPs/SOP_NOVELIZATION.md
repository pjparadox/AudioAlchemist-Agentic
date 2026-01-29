# SOP — Novelization Protocol (Script to Bestseller)

## Objective
Convert a Screenplay/Transcript into a high-density Literary Novel (>70,000 words) that emulates a specific author's voice.

## Team
*   **Varys:** Research Director (Lead).
*   **Proteus:** Style Analyst (The Eyes).
*   **Mercury:** Researcher (The Context).
*   **Elara:** Ghost Writer (The Expander).
*   **Lyra:** Prose Stylist (The Voice).
*   **Thoth:** QC Supervisor (The Gatekeeper).
*   **Huy:** Vietnamese Reviewer (The Reality Check).

---

## Phase 1: Style Acquisition (The Setup)
**Goal:** Create a `STYLE_PROFILE.md` that defines the target voice.

1.  **Ingest:** Place author writing samples (PDF/DOCX) in `input_quill/style references/`.
2.  **Analyze (Proteus):**
    *   Proteus reads the samples.
    *   Analyzes sentence structure, dialogue tags, and sensory focus.
    *   Drafts the Profile.
3.  **Contextualize (Mercury):**
    *   Mercury searches online for author interviews and critiques.
    *   finds "Dialogue Best Practices".
4.  **Audit (Varys):**
    *   Varys compares Proteus's draft with Mercury's data.
    *   **Output:** Final `STYLE_PROFILE_[Author].md`.

---

## Phase 2: Ghost Writing (The Expansion)
**Goal:** Convert sparse script into dense prose.
**Agent:** **Elara**.

1.  **Input:** Split the script into small chunks (e.g., 5-10 pages).
2.  **Process:**
    *   **Ratio:** Expand 1 line of action -> 3 paragraphs of prose.
    *   **Injection:** Interrupt dialogue with internal monologue and sensory details.
    *   **Physiology:** Describe the physical sensations of the characters (sweat, pulse, adrenaline).
    *   **Setting:** Turn "EXT. ALLEY - NIGHT" into a full atmospheric description.
3.  **Output:** A "Zero Draft" that is texturally rich but maybe stylistically generic.

---

## Phase 3: Style Infusion (The Polish)
**Goal:** Apply the Author's Voice.
**Agent:** **Lyra**.

1.  **Input:** Elara's Zero Draft + `STYLE_PROFILE.md`.
2.  **Process:**
    *   **Voice Match:** Rewrite sentences to match the author's rhythm (e.g., King's folksy horror vs. Hemingway's brevity).
    *   **Dialogue Tags:** **REMOVE "SAID".** Replace with action beats or implied speakers.
    *   **Fusion:** If multiple authors are requested, blend their traits.
3.  **Output:** Stylized Manuscript.

---

## Phase 4: The Thoth Gate (QC)
**Goal:** Ensure market readiness and length.
**Agent:** **Thoth**.

1.  **The 70k Rule:**
    *   Estimate total length based on current chunk expansion.
    *   If projected length < 70,000 words: **REJECT.**
    *   Instruction: "Go back and expand the sensory details of the environment."
2.  **Quality Check:**
    *   Does it read like a movie or a book? (Must be a book).
    *   Is the voice consistent?
3.  **Verdict:** Approved or Revision Order.

---

## Phase 5: Localization (Vietnamese)
**Goal:** Translate to native-level Vietnamese.
**Agents:** **Lyra (Translator)** + **Huy (Reviewer)**.

1.  **Translate (Lyra):** Convert to Vietnamese, preserving the *literary effect* (not just meaning).
2.  **Review (Huy):**
    *   Huy reads the Vietnamese output *without* looking at the English.
    *   **Flag:** Any line that sounds "Tây" (Western) or uses passive voice awkwardly.
    *   **Report:** "Line 42 sounds fake. A real Vietnamese person would say..."
3.  **Final Polish:** Lyra applies Huy's notes.
