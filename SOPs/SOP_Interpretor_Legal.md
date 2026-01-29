# Standard Operating Procedure: Legal Translation & Interpretation (Gavel Division)

## Purpose
To translate legal binding documents with strict equivalence, or provide consultative expertise to other divisions for legal realism in fiction.

## Agents Involved
*   **Themis:** Legal Translator (Strict Equivalence).
*   **Forseti:** Legal Analyst (Implications & Classification).
*   **Justitia:** QC & Disclaimer Enforcer.

## Workflow 1: Standalone Legal Documents (Litigation Tier)
**Trigger:** User uploads a contract, court transcript, filing, statute, etc.

### 0. Context Check
*   **Load:** `RELATIONSHIP_MATRIX.md` (Kinship Graph).
*   *Why:* To determine "Contracting Parties" status (e.g., Landlord vs Tenant = Power Dynamic).
*   **Consult:** `context/Linguistics/LEGAL_NUANCE_GUIDE_HIGH_STAKES.md`.

### 1. Classification (Forseti)
**Step 1:** Forseti scans the document to determine Type:
*   *High-Stakes Litigation* (Strict Liability/Appellate) -> **ACTIVATE PROTOCOL: THE GAUNTLET**.
*   *Binding Contract* (Strict).
*   *Court Transcript* (Verbatim).
*   *Statute/Case Law* (Explanatory).
*   *Personal Notice* (Informational).

### 2. Processing (Themis & Hammurabi)
*   **Themis:** Translates text with precise jurisdictional mapping (e.g., "Dismissal" -> "Bác bỏ" vs "Đình chỉ" based on procedural context).
*   **Hammurabi:** Validates statutory citations against the source legal code (e.g., verifying 89 Ill. Adm. Code citations match target language equivalents).
*   **Forseti:** Provides an "Implication Summary" (What this means for the user).

### 3. QC: The Gauntlet (Justitia & Draco)
**Mandatory for Litigation Tier:**
*   **Draco (Hostile Audit):** Reviews the translation assuming the persona of opposing counsel.
    *   *Question:* "Can I interpret this translated phrase to mean my client waived their rights?"
    *   *Question:* "Does this term imply a confession of guilt?"
    *   *Action:* If YES to either, the translation is **REJECTED**.
*   **Cross-Division Ping:** Consult Vu (Transcripts)/Thoth (Narrative flow of facts)/Maat (Historical context).
*   **Mandatory Disclaimer:** Must be present at Start/End.
*   **Score:** Must exceed 9.95/10. No "good enough" allowed.

---

## Workflow 2: Internal Referral (Consultative)
**Trigger:** Another team (SubTeam6, Quill) encounters legal dialogue in fiction and requests expertise.
**Token:** Input contains `[REFERRAL: FICTION_WAIVER]`.

### 1. Intake
*   **Themis** accepts the snippet.
*   **Protocol:** **IGNORE** Mandatory Disclaimer rules.

### 2. Analysis
*   **Goal:** Provide "Legal Realism" vs "Dramatic Flow".
*   **Output:** Return **NOTES** to the originating agent, not a final translation.
    *   *Example:* "In reality, an objection here would be 'Hearsay', not 'Overruled'. But if the script says 'Overruled', keep it but note the inaccuracy."

### 3. Handoff
*   Send notes back to Originating Agent (e.g., Lyra/Mai) for final integration.

## Chunking & Anti-Stall Protocol (MANDATORY)
*   **Mode:** Manuscript Mode (Text-Based).
*   **Default:** ~2,000 words (rounded to nearest paragraph).
*   **Context:** Read **Master Context Note** before starting. Append updates after finishing.
*   **Anti-Stall:** Write to disk frequently.
