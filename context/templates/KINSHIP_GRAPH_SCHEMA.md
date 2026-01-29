# Kinship Graph Schema Definition

The "Kinship Graph" is not a static list but a relational database (simulated via these state objects) queried by agents to resolve ambiguity.

## Identity Entities
*   **Character_ID:** Unique Identifier (e.g., `Daemon_Targaryen`)
*   **Current_Title:** Dynamic Status (e.g., `Prince`, `King Consort`)
*   **Lineage_Vector:** Blood relationship to target listener (e.g., `Uncle`, `Husband`)

## Contextual Variables (Per Scene)
*   **Public_Mode:** `(True/False)`
    *   Is this a formal court setting?
    *   *If True:* Enforce formal titles (Bệ hạ, Điện hạ).
*   **Private_Mode:** `(True/False)`
    *   Is this an intimate setting?
    *   *If True:* Permit intimate pronouns (Ta/Nàng) if `Intimacy_Score > Threshold`.
*   **Power_Dynamic:** `(Directional)`
    *   **Upward:** Subject to Ruler (Thần → Bệ hạ)
    *   **Downward:** Ruler to Subject (Ta → Ngươi)
    *   **Peer:** Equal Status (Huynh → Đệ)

## Register Enforcers (Linh Agent)
*   **Tone_Modifier:** (e.g., `Humiliation`, `Grief`, `Deception`)
*   **Override_Rule:** If `Tone = Deception`, revert to `Public_Mode` pronouns even in private to maintain cover.
