import os

ROOT_DIR = "."
PROJECT_DIR = os.path.join(ROOT_DIR, "Context", "projects", "The_Exorcism_of_Emily_Rose")

CONTENT_STYLE = """# STYLE_GUIDE.md: The Exorcism of Emily Rose

## 1. The Core Mechanic: Register Collision
The translation must maintain four distinct "Fonts" (Registers) that never blend.

| Register | Tone | Vietnamese Strategy | Japanese Strategy | Korean Strategy |
| :--- | :--- | :--- | :--- | :--- |
| **LEGAL** | Procedural, Weaponized Politeness. | Formal ("Thưa Tòa", "Tôi"). No slang. | **Lv2 (Keigo/Kenjougo).** | **LvA (Hapsyo-che).** |
| **CLINICAL** | Objective, Diagnostic. | Formal Technical. No hedging. | **Lv2 (Academic).** | **LvA (Institutional).** |
| **RELIGIOUS** | Ritual, Spiritual Authority. | Catholic Standard ("Cha", "Nghi thức"). | **Lv3 (Liturgical).** | **LvD/LvA Hybrid.** |
| **DEMONIC** | Contempt, Inversion. | Archaic Dominance ("Ta/Ngươi") -> Raw Hate ("Mày"). | **Lv3 -> Lv0.** | **LvE (Banmal + Contempt).** |

## 2. The Demon Voice Escalation Protocol
* **Phase 1 (Whisper):** "Ta... Ngươi..." (Controlled contempt).
* **Phase 2 (Voice):** Harsher address. Imperatives.
* **Phase 3 (The Voices):** Multiplicity. "Mày" used for humiliation.
* **Named Entities (Lucifer):** Regal Calm. Absolute certainty.

## 3. Erin Bruner's Arc
* **Early Erin:** "Lawyer Distance" (Legal nouns).
* **Late Erin:** "Moral Investment" (Human nouns).
"""

CONTENT_VOICES = """# CHARACTER_VOICES.md

## ERIN BRUNER (Defense)
* **Address:** "Tôi" (Self). "Thưa Tòa" (Court). "Cha Moore" (Respectful distance).
* **Shift:** Moves from "Winning a case" to "Defending a soul."

## FATHER RICHARD MOORE (Defendant)
* **Vibe:** Disciplined, Intense.
* **Address:** "Cô Bruner" (Polite).
* **Constraint:** NOT chatty. Controlled emotion.

## OWEN THOMAS (Prosecutor)
* **Vibe:** Predatory Tactician. "Reasonable" Aggression.
* **Strategy:** Weaponized Politeness. Trap with logic, don't yell.

## JUDGE BREWSTER
* **Vibe:** Procedural Gravity. Ultra-brief. "Chấp nhận." "Bác bỏ."

## KARL GUNDERSON (The Boss)
* **Vibe:** Status-Aware. "Win/Perform" logic.
* **VN:** "Anh/Ông Karl" (Seniority).

## EMILY ROSE
* **Mode A (Emily):** Gentle, Frightened. Pleading.
* **Mode B (The Demon):** See Demon Voice Protocol.

## DR. VOGEL / MAREK / BRIGGS
* **Vibe:** Clinical Certainty. They own reality. No uncertainty.
"""

CONTENT_RELATIONS = """# RELATIONSHIP_MATRIX.md

## ERIN ↔ KARL
* **Dynamic:** Senior/Subordinate.
* **Shift:** Karl appeals to optics; Erin stands firm.

## ERIN ↔ FATHER MOORE
* **Dynamic:** Attorney/Client -> Moral Allies.
* **Early:** Professional distance. **Late:** Warmer rhythm, formal titles.

## EMILY ↔ FAMILY
* **Parents:** "Con" (Self), "Mẹ/Ba" (Address). Pleading.
* **Alice:** "Chị/Em" (Sibling markers mandatory).
"""

CONTENT_GLOSSARY = """Term,Category,Vietnamese,Context
Objection,Legal,Phản đối,Courtroom
Sustained,Legal,Chấp nhận,Judge
Overruled,Legal,Bác bỏ,Judge
Witness,Legal,Nhân chứng,Courtroom
Defendant,Legal,Bị cáo,Courtroom
Prosecution,Legal,Bên công tố,Pick ONE
Defense,Legal,Bên bào chữa,Courtroom
Verdict,Legal,Phán quyết,Endgame
Sentence,Legal,Tuyên án,Endgame
Priest / Father,Religious,Cha,Title
Exorcism,Religious,Nghi thức trừ tà,Pick ONE
Demon,Religious,Ác quỷ,Pick ONE
Possession,Religious,Bị ám,Context Dependent
Anneliese Michel,Reference,Anneliese Michel,History
Dr. Adani,Character,Dr. Adani,Treat Adant as Adani
"""

CONTENT_TRIGGERS = """# TRANSLATION_TRIGGERS.md

## PHASE 1: CAREER CASE
* **Trigger A (Assignment):** Karl frames case as "Reputation."
* **Trigger B (Jail Meeting):** First meeting with Moore. Erin keeps professional distance.

## PHASE 2: CRACKS
* **Trigger F (3:00 AM Intrusion):** Erin's first supernatural experience. Drop lawyer voice. Fear is immediate.
* **Trigger G (Evidence):** Erin hears the tape. Reduce legal jargon. Increase ethical language.

## PHASE 3: AUTHORITY COLLISION
* **Trigger D (Medical Testimony):** Doctors claim reality. High confidence clinical lexicon.
* **Trigger H (Demon Voice):** Escalation from Whisper -> Voice -> Voices.
* **Trigger I (Ritual):** Father Moore commands. Formulaic Catholic commands.

## PHASE 4: MEANING
* **Trigger K (Closing):** Value-heavy language. Controlled conviction.
* **Trigger M (Sentencing):** The Moral Paradox. Judge is procedural. Moore is spiritually grounded.
"""

CONTENT_SCENES = """# SCENE_BEATS.md

## SCENE INDEX
* **7A:** Erin, Karl (Career framing).
* **10 (Jail):** Erin, Moore (First meeting).
* **17-19 (Court):** Judge, Owen, Erin (Trial rules).
* **20-26 (Medical):** Dr. Vogel, Dr. Marek (Clinical dominance).
* **86 (Exorcism):** Father Moore (Ritual Command).
* **87 (Demon):** The Voices / Lucifer (Dominance).
* **111 (Verdict):** Jury Foreman.
* **112 (Sentencing):** Judge, Moore.
* **113 (Fallout):** Erin, Karl.
"""

def write_file(path, content):
    with open(path, "w", encoding="utf-8") as f: f.write(content)
    print(f"[GENERATED] {path}")

def main():
    print("--- INSTALLING EMILY ROSE PROJECT (COMPLETE) ---")
    if not os.path.exists(PROJECT_DIR): os.makedirs(PROJECT_DIR)
    write_file(os.path.join(PROJECT_DIR, "STYLE_GUIDE.md"), CONTENT_STYLE)
    write_file(os.path.join(PROJECT_DIR, "CHARACTER_VOICES.md"), CONTENT_VOICES)
    write_file(os.path.join(PROJECT_DIR, "RELATIONSHIP_MATRIX.md"), CONTENT_RELATIONS)
    write_file(os.path.join(PROJECT_DIR, "GLOSSARY.csv"), CONTENT_GLOSSARY)
    write_file(os.path.join(PROJECT_DIR, "TRANSLATION_TRIGGERS.md"), CONTENT_TRIGGERS)
    write_file(os.path.join(PROJECT_DIR, "SCENE_BEATS.md"), CONTENT_SCENES)
    print("Emily Rose Installed (Registers + Voices + Triggers).")

if __name__ == "__main__":
    main()