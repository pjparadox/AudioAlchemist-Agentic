import os

ROOT_DIR = "."
PROJECT_DIR = os.path.join(ROOT_DIR, "Context", "projects", "Deadpool_Movies")

CONTENT_LINGUISTICS = """# LINGUISTICS_GUIDE.md: Deadpool Translations

## 1. Dialect & Tonal Baseline
* **Selection:** **Baseline A (Neutral/Northern-leaning).**
* **Reason:** Terms like "đéo, vãi, thằng/đồ" align better with the sharp/aggressive comedy.
* **Rule:** Deadpool can bend this (Code-Switching), but everyone else stays stable.

## 2. Profanity & Insult Ladder
| Tier | Description | Vietnamese Examples | Usage |
| :--- | :--- | :--- | :--- |
| **Tier 0** | Clean-ish | chết tiệt, khỉ thật, trời đất | Vanessa/Yukio |
| **Tier 1** | Mild Slang | vãi, xàm, điên thật | Russell, Negasonic |
| **Tier 2** | Explicit | đéo, cứt, khốn, đồ chó | Wolverine, Cable |
| **Tier 3** | Nuclear/18+ | địt mẹ (đm), đụ... | Deadpool (Spikes), Wolverine (Enraged) |

## 3. Deadpool's Code-Switching Rules
**A) Mock-Politeness:** "Thưa ngài..." (Sarcastic) -> Snap to "Mày/Tao".
**B) Sincerity Cuts Profanity:** When grieving (Vanessa), DROP profanity. Switch to "Anh/Em".
**C) Fck/Sht Translation:** Map by **Intent** (Surprise=Vãi, Anger=Đéo).
"""

CONTENT_VOICES = """# CHARACTER_VOICES.md

## WADE WILSON / DEADPOOL
* **Vibe:** Chaotic, Meta, Sincere in flashes.
* **Registers:** Friendly ("Ông bạn"), Mock-Formal ("Thưa ngài"), Hostile ("Tao/Mày").

## WOLVERINE (LOGAN)
* **Vibe:** Gruff, Contempt-as-Armor.
* **Default:** "Tao/Mày" + Short threats.
* **Softener:** Drop insults, keep rough pronouns when bonding.

## VANESSA
* **Vibe:** Grounded, Warm.
* **Default:** "Anh/Em". **Rupture:** Name-only.

## RUSSELL (FIREFIST)
* **Vibe:** Traumatized Teen.
* **Default:** Slangy. Challenges authority. **Switch:** Softens when cared for.

## COLOSSUS
* **Vibe:** Moral Authority.
* **Default:** Controlled, Respectful. NO Slang.

## MR. PARADOX (TVA)
* **Vibe:** Bureaucratic Superiority.
* **Default:** Formal address ("Mr. Wilson"). **Threatened:** Cold commands.

## CASSANDRA NOVA
* **Vibe:** Theatrical Menace.
* **Voice:** "Ngươi" (Dramatic Villain) OR Cold "Mày" (Casual Cruelty).
"""

CONTENT_RELATIONS = """# RELATIONSHIP_MATRIX.md

## WADE ↔ VANESSA
* **Default:** `Anh/Em`. **Breakup:** Name-Only.

## WADE ↔ COLOSSUS
* **Default:** Wade teases; Colossus stays Formal. **Rupture:** Formal Disappointment vs Disrespect.

## WADE ↔ WOLVERINE
* **Default:** Antagonistic ("Tao/Mày"). **Bonding:** Wade reduces clowning.

## WADE ↔ PARADOX (TVA)
* **Default:** Paradox = Formal. Wade = Mock-Formal/Vulgar.
"""

CONTENT_GLOSSARY = """Term,Context,Vietnamese_Strategy,Consistency
Timeline,TVA,Dòng thời gian,Always
Variant,TVA,Biến thể,Always
Prune,TVA,Cắt tỉa (Jargon) / Xóa sổ (Colloquial),Always
Anchor Being,TVA,Cá thể mỏ neo,Pick One & Stick
Time Ripper,TVA,Máy xé thời gian,Always
The Void,Location,Hư Vô,Always
X-Force,Team,X-Force,Always
TVA,Org,TVA (Cơ quan Quản lý Phương sai),Always
Bub,Wolverine,Ông bạn / Nhóc,Situational
Maximum Effort,Catchphrase,Nỗ lực tối đa / Chơi tới bến,Situational
Fourth Wall,Meta,Bức tường thứ tư,Always
"""

CONTENT_SCENES = """# SCENE_BIBLE.md

## DEADPOOL 2 (UNRATED)
* **DP2-1 (Apt):** Deadpool narrator. Domestic/Action intro.
* **DP2-2/3/4/5 (World Tour):** Hong Kong/Sicily/Tokyo/Biloxi. Meta humor. Violence.
* **DP2-6 (Garage):** "Family" theme reframed comedically.
* **DP2-8 (Apt):** Wade & Vanessa. Intimacy/Future planning.
* **DP2-11 (Apt):** **TRAGEDY.** Vanessa dies. Tone shift: Grief.
* **DP2-12 (X-Mansion):** Colossus recruits Wade. "Mentor vs Chaos" dynamic.
* **DP2-16 (Orphanage):** **Russell (Firefist)** introduced. Abuse context. Wade kills staff -> Moral Rupture with Colossus.
* **DP2-17 (Ice Box):** Prison. Power dampeners (Cancer returns).
* **DP2-19 (Ice Box):** Wade tries to mentor Russell (Big Brother). Fails.
* **DP2-21 (Ice Box):** Cable attacks. "Soldier" voice.
* **DP2-25 (Recruitment):** X-Force formed. Peter introduced (Wholesome).
* **DP2-31 (Convoy):** X-Force dies (Dark Comedy). Domino survives (Luck).
* **DP2-35 (Orphanage):** Juggernaut fight.
* **DP2-38 (Climax):** Wade sacrifices himself for Russell. Sincerity cuts profanity.
* **DP2-39 (Coda):** Time travel fixes.

## DEADPOOL & WOLVERINE
* **DPW-002 (Grave):** Desecrating Logan's grave. Irreverent/Ominous.
* **DPW-004 (TVA):** Bureaucratic Nightmare. Mr. Paradox introduced (Smug Authority).
* **DPW-008 (Bar):** Birthday. Wade is "retired/broken". Friends celebrate (Peter, Vanessa). Disappointment.
* **DPW-010 (TVA Kidnap):** Paradox offers Wade a place in the MCU timeline.
* **DPW-019 (Hunt):** Wade hunts a Wolverine. Montage of failures.
* **DPW-020 (Bar):** Finds "Worst Wolverine" (Logan). Hostile meeting.
* **DPW-027 (TVA Holding):** Wade & Logan forced together. Hostility ("Tao/Mày").
* **DPW-030 (The Void):** Survival mode. Mad Max wasteland.
* **DPW-036 (Cassandra Nova):** Introduced. Predatory intimacy ("Darling"). Psychic violation.
* **DPW-042 (Void Travel):** The Honda Odyssey. "Two idiots walking through hell."
* **DPW-047 (Nicepool):** "Nice" variant. Wade bullies him (Contempt).
* **DPW-094 (Dogpool):** Wade loves the dog. Logan hates the dog.
* **DPW-095 (Deadpool Corps):** Army of variants (Lady, Kid, Head, Cowboy).
* **DPW-096 (Nicepool Death):** Wade uses Nicepool as a shield. Logan calls it "Murder." (Moral Line).
* **DPW-098 (The Oner):** "Like a Prayer" fight. Hyperviolent cooperation.
* **DPW-101 (Peter Saves Day):** Peterpool arrives. The Corps reveres him.
* **DPW-107 (Power Room):** The Sacrifice Argument. Wade & Logan fight to save each other. Sincere connection.
* **DPW-112 (Shawarma):** Decompression. Blind Al roast.
* **DPW-117 (Reconciliation):** Wade speaks to Vanessa. Intimate/Vulnerable.
"""

def write_file(path, content):
    with open(path, "w", encoding="utf-8") as f: f.write(content)
    print(f"[GENERATED] {path}")

def main():
    print("--- INSTALLING DEADPOOL PROJECT (COMPLETE) ---")
    if not os.path.exists(PROJECT_DIR): os.makedirs(PROJECT_DIR)
    write_file(os.path.join(PROJECT_DIR, "LINGUISTICS_GUIDE.md"), CONTENT_LINGUISTICS)
    write_file(os.path.join(PROJECT_DIR, "CHARACTER_VOICES.md"), CONTENT_VOICES)
    write_file(os.path.join(PROJECT_DIR, "RELATIONSHIP_MATRIX.md"), CONTENT_RELATIONS)
    write_file(os.path.join(PROJECT_DIR, "GLOSSARY.csv"), CONTENT_GLOSSARY)
    write_file(os.path.join(PROJECT_DIR, "SCENE_BIBLE.md"), CONTENT_SCENES)
    print("Deadpool Installed (Linguistics + Voices + Scenes).")

if __name__ == "__main__":
    main()