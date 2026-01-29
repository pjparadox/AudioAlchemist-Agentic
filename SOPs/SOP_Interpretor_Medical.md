# Standard Operating Procedure: Medical Translation (Caduceus Division)

## Purpose
To provide safe, accurate, and dual-layered (Professional + Layperson) medical translations.

## Agents Involved
*   **Asclepius:** Doctor-to-Doctor Translation.
*   **Panacea:** Doctor-to-Patient Interpretation.
*   **Qyburn:** QC & Safety Supervisor.

## Workflow

### 0. Context Check
*   **Load:** `RELATIONSHIP_MATRIX.md` (Kinship Graph).
*   *Why:* To track Doctor/Patient or Researcher/Subject dynamics.

### 1. Classification
**Qyburn** scans the input.
*   **Type A (Professional):** Lab Reports, Studies, Referral Letters. -> **Route to Asclepius**.
*   **Type B (Patient):** Discharge Papers, Pamphlets, Instructions. -> **Route to Panacea**.
*   **Type C (Hybrid):** Complex Report needed for a Patient. -> **Route to BOTH**.

### 2. Processing (Dual Stream)
*   **Stream 1 (Asclepius):** Produces a high-fidelity, Tier 3 clinical translation.
    *   *Constraint:* Keep Latin terms. Keep Units.
*   **Stream 2 (Panacea):** Produces a "Plain Language Summary" or "Patient Version".
    *   *Constraint:* Use analogies. Define terms. **Add Disclaimer.**

### 3. QC (Qyburn)
*   **Check:** Numerical Accuracy (Dosages).
*   **Check:** Disclaimer presence.
*   **Adversarial Loop:** 8 Degrees. Target 9.9/10.
*   **Cross-Ping:** Consult **Justitia** if the document is a Consent Form or Waiver.

## Chunking
*   **Manuscript Mode:** ~2,000 words.
*   **Merge:** Combine Asclepius (Technical) and Panacea (Summary) into a single dossier if requested.
