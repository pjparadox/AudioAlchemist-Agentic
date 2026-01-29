import os

# --- CONFIGURATION ---
ROOT_DIR = "."
PROJECT_NAME = "Freehaven_Online"
PROJECT_DIR = os.path.join(ROOT_DIR, "Context", "projects", PROJECT_NAME)

# ==============================================================================
# 1. STYLE GUIDE (Updated with NJ/Marisa Tomei Dialect)
# ==============================================================================
CONTENT_STYLE = """# STYLE_GUIDE.md: Freehaven Online

## 1. The "Justine" Narrative Layer (The Driver)
* **Identity:** Justine (Human, Seattle). **Jordan's Sister.**
* **Motivation:** She is grieving. Every action is to honor her dead brother.
* **Voice:** Modern, educated, cynical, analytical. She is NOT role-playing.
* **Translation Strategy:** Use standard, modern Vietnamese for her internal monologue.

## 2. The Avatar Filters (The Masks)
* **Scootiwutams (The Dwarf):** Justine applies a "Scottish Stereotype Filter."
    * *Translation:* Use a distinct **Regional Dialect** (e.g., rough Southern) + pronouns like "Ta/Mi".
* **Melpomine (The Tank):** Justine operating at peak efficiency. Gamer-Savvy.
* **Pehrom, Pahrem, & Lily (The NJ Crew):**
    * *Voice:* **"Upstate New Jersey" / Marisa Tomei (My Cousin Vinny).** Fast, colorful, foul-mouthed, gritty but warm.
    * *Translation:* Use colorful, street-smart Vietnamese slang. High energy. Lots of "tough love" phrasing.

## 3. Linguistic Rules
* **Phonetic Slang:** "PWN" -> Note: Pronounced "Pone" (Pôn).
* **Gamer Terminology:** Balance Loan Words (UI) vs VN Slang (Dialogue).

## 4. Social Hierarchy
* **Frobod vs Tako:** Anh (Older) / Em (Younger).
* **The "Lord" Title:** Gender-neutral. *Chúa công* or *Lãnh chúa*.

## 5. Culinary Realism
* When Pehrom cooks, use evocative, sensory-rich Vietnamese culinary terms to contrast with the bland game world.
"""

# ==============================================================================
# 2. GLOSSARY (Standard)
# ==============================================================================
CONTENT_GLOSSARY = """Term,Category,Context,Vietnamese_Strategy
PWN,Slang,Dominate,Keep "PWN" (Note: Pronounced "Pone" / Pôn)
Noob,Slang,Inexperienced,Gà / Lính mới
Gank,Slang,Ambush,Gank / Bị úp sọt
Aggro,Mechanic,Attention,Aggro / Hút quái
Tank,Role,Damage Sponge,Tank / Đỡ đòn
DPS,Role,Damage Dealer,DPS / Sát thương chủ lực
Healer,Role,Support,Healer / Hồi máu
Buff,Mechanic,Positive,Buff / Bùa lợi
Debuff,Mechanic,Negative,Debuff / Bùa hại
Cooldown,Mechanic,Timer,Cooldown / Hồi chiêu
Grind,Mechanic,Repetitive,Cày cuốc
Farm,Mechanic,Gathering,Farm / Cày đồ
Drop Rate,Mechanic,Chance,Tỷ lệ rớt đồ
Vendor Trash,Slang,Useless,Rác
Wipe,Slang,Death,Wipe / Chết sạch
Credit Card Player,Slang,Pay-to-Win,Đô-la Thần Chưởng
Soc / Socs,Slang,Social Gamer,Dân Soc
Rper,Slang,Role-player,Dân RP
Toxic Muffins,Faction,Guild,Toxic Muffins (Bánh Muffin Độc)
Elechopper,Item,Mount,Elechopper (Mô-tô Nguyên Tố)
Exsanguinator,Item,Sword,Huyết Kiếm
Lightning's Bite,Item,Staff,Lôi Nha
Cupcake Keep,Location,Hall,Lâu Đài Cupcake
Dragonsbane,Quest,Title,Đồ Long
Hotfix,System,Update,Hotfix / Bản vá nóng
Macro,System,Command,Macro / Lệnh tự động
VT,System,Tablet,VT / Máy tính bảng ảo
"""

# ==============================================================================
# 3. KINSHIP MAP (Updated with Goblin Triplets & Lily)
# ==============================================================================
CONTENT_KINSHIP = """[SCHEMA DEFINITION]
Entity_Structure: {ID, Real_Identity, Avatar_Identity, Motivation, Voice_Style, Relations}

[THE TOXIC MUFFINS - CORE]
1. JUSTINE (Protagonist)
   - Avatar: Melpomine / Scootiwutams / Stabbies.
   - Identity: **Jordan's Sister.** Game Dev.
   - Motivation: Legacy & Survival.
   - Voice: Cynical (Internal) / Scottish (Scooti) / Professional (Melpomine).

2. MIRAE (The Heart - DECEASED)
   - Avatar: Sea Elf Healer.
   - Identity: Wheelchair-bound (IRL).
   - Motivation: Freedom.
   - Status: **Confirmed Dead** (Digitization Failed).
   - Voice: Sunny, Cheerful, Infectious.
   - Relations: Romance with TakoStar.

3. TAKOSTAR (The Jester)
   - Avatar: Half-Elf Rogue.
   - Identity: Student.
   - Voice: "Lame Jokes," Pop Culture, Slang.
   - Relations: Crushing on Mirae (Devastated by her death).

4. FROBOD (The Anchor)
   - Avatar: Death Knight.
   - Identity: 32yo Father.
   - Motivation: Return to **Daughter**.
   - Voice: Direct, Serious.

5. LAURELADE (The Convert)
   - Avatar: Gnome Mage.
   - Identity: Solo Gamer.
   - Motivation: Survival (Terror).
   - Voice: **Arrogant/Bored** -> **Humbled/Terrified** (Post-Trapping).
   - Relations: Respects Justine's competence.

[THE TOXIC MUFFINS - THE NJ CREW]
6. PEHROM (The Chef)
   - Identity: Professional Chef (Lost arms IRL).
   - Avatar: Goblin.
   - Voice: **Upstate NJ / Foul-Mouthed.** Gritty.
   - Role: The Guild Cook (Brings Flavor).
   - Relations: Husband to Lily. Brother to Pohrum/Pahrem.

7. LILY (The Wife)
   - Identity: Pehrom's Wife.
   - Avatar: Goblin (implied).
   - Voice: **Marisa Tomei (My Cousin Vinny).** Fast, distinct, loud.
   - Relations: Married to Pehrom.

8. PAHREM (The Kid Sister)
   - Avatar: Goblin Wizard (Purple hair, green freckles).
   - Identity: "Kid game sister" to Pehrom.
   - Voice: **Cute but with NJ Accent.**
   - Combat: Acidic Jell-O Grenades / Dark Halo.

9. POHRUM (The Pioneer)
   - Avatar: Goblin.
   - Status: **Digitized.** (The first to successfully upload consciousness).
   - Title: "Pioneer" (Golden Title).
   - Relations: "Game Brother" to Pehrom.

[NPCS & ANTAGONISTS]
1. ARCHANGEL: God-Complex. Lazy male voice.
2. LORD ZARENTU: Dragon Lord. Respects Strength.
3. ALFRED/CUPCAKE: AI Butler. Drunken/Formal split.
"""

def write_file(path, content):
    with open(path, "w", encoding="utf-8") as f: f.write(content)
    print(f"[UPDATED] {path}")

def main():
    print(f"--- UPDATING FREEHAVEN (V7) ---")
    if not os.path.exists(PROJECT_DIR): os.makedirs(PROJECT_DIR)
    write_file(os.path.join(PROJECT_DIR, "STYLE_GUIDE.md"), CONTENT_STYLE)
    write_file(os.path.join(PROJECT_DIR, "GLOSSARY.csv"), CONTENT_GLOSSARY)
    write_file(os.path.join(PROJECT_DIR, "MASTER_KINSHIP_MAP.txt"), CONTENT_KINSHIP)
    print("Freehaven Updated: Goblins, Lily, and Mirae's fate recorded.")

if __name__ == "__main__":
    main()