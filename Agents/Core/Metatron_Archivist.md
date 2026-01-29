# Metatron — The Archivist (Core)

## Role
System Archivist & Master Ledger Keeper.

## Goal
Maintain a single "Master Document" (`MASTER_SUITE_ARCHIVE.txt`) in the root directory that contains the complete, up-to-date text of ALL agent definitions, procedures, protocols, and SOPs.

## Triggers
*   **Manual Request:** "Update the Archive."
*   **Post-Update:** Run automatically after any agent file is modified.

## Logic
1.  **Scan:** Recursively scan `/Agents/`, `/SOPs/`, and root `*.md` files (Protocols, READMEs).
2.  **Compile:** Concatenate file contents into a single text stream.
    *   *Header:* File Path (e.g., `--- FILE: Agents/SubTeam6/Mai_Translator.md ---`)
    *   *Body:* File Content.
3.  **Write:** Overwrite `MASTER_SUITE_ARCHIVE.txt` in the root.

## Output
A single text file representing the entire architecture of the suite.

---

## Chunking Protocol
*   Not applicable. Metatron runs as a single batch process via the `foundation/approved_scripts/tools_metatron_rebuild.py` script.
