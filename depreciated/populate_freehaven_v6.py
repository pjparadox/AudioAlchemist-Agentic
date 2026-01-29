import os

# --- CONFIGURATION ---
ROOT_DIR = "."
PROJECT_NAME = "Freehaven_Online"
PROJECT_DIR = os.path.join(ROOT_DIR, "Context", "projects", PROJECT_NAME)

# ==============================================================================
# 1. STYLE GUIDE (Phonetics, Dialects, & Social Hierarchy)
# ==============================================================================
CONTENT_STYLE = """# STYLE_GUIDE.md: Freehaven Online

## 1. The "Justine" Narrative Layer (The Driver)
* **Identity:** Justine (Human, Seattle). **Jordan's Sister.**
* **Motivation:** She is grieving. Every action is to honor her dead brother.
* **Voice:** Modern, educated, cynical, analytical. She is NOT role-playing; she is speaking as herself *through* the avatar.
* **Translation Strategy:** Use standard, modern Vietnamese for her internal monologue.

## 2. The Avatar Filters (The Masks)
* **Scootiwutams (The Dwarf):** Justine applies a "Scottish Stereotype Filter."
    * *Translation:* Use a distinct **Regional Dialect** (e.g., rough Southern or specific rural vocabulary) to mimic this "Foreign/Rough" persona. Use pronouns like "Ta/Mi" or "Lão/Nhóc".
* **Melpomine (The Tank):** Justine operating at peak efficiency.
    * *Translation:* Sharp, direct, Gamer-Savvy.
* **Pehrom (The Chef):** "Upstate New Jersey" / Gritty / Foul-mouthed.
    * *Translation:* Use gritty, street-level Vietnamese slang. Lots of cursing ("Mẹ kiếp", "Chó chết").

## 3. Linguistic Rules
* **Phonetic Slang:** If a term has no direct translation, use the English term but provide a **Phonetic Guide** or footnote on first use so the reader hears it correctly.
    * *Example:* "PWN" -> Note: Pronounced "Pone" (Pôn). Meaning: Dominate.
* **Gamer Terminology:** Balance between "Loan Words" (Tank, DPS) and "Vietnamese Gamer Slang" (Trâu bò, Máu giấy).
    * *Guideline:* If it's a UI element, use the Loan Word. If it's characters talking trash, use the VN Slang.

## 4. Social Hierarchy & Honorifics
* **Frobod (32yo) vs TakoStar (Student):**
    * Frobod = *Anh* (Older Brother figure).
    * Tako = *Em* (Younger Brother figure).
* **Guild Leader (Justine):**
    * Despite the age gap, Tako shows her "Professional Respect."
* **The "Lord" Title:** Gender-neutral in this world. "Lord Scootiwutams" (Female Dwarf) -> *Chúa công* or *Lãnh chúa* (keep it heavy/respectful).

## 5. Culinary Realism
* Food is a major theme. The transition from "Tasteless" to "Flavorful" is a plot beat.
* *Directive:* When Pehrom cooks, use evocative, sensory-rich Vietnamese culinary terms (fragrance, texture, heat) to contrast with the bland game world.
"""

# ==============================================================================
# 2. GLOSSARY (Updated with Phonetics & User Corrections)
# ==============================================================================
CONTENT_GLOSSARY = """Term,Category,Context,Vietnamese_Strategy
PWN,Slang,Gamer Slang for Dominate,Keep "PWN" (Note: Pronounced "Pone" / Pôn)
Noob,Slang,Inexperienced Player,Gà / Lính mới (Phonetic: Núp if loaning)
Gank,Slang,Unfair Ambush,Gank / Bị úp sọt
Aggro,Mechanic,Enemy Attention,Aggro / Hút quái
Tank,Role,Damage Sponge,Tank / Đỡ đòn
DPS,Role,Damage Dealer,DPS / Sát thương chủ lực
Healer,Role,Support,Healer / Hồi máu
Buff,Mechanic,Positive Effect,Buff / Bùa lợi
Debuff,Mechanic,Negative Effect,Debuff / Bùa hại
Cooldown,Mechanic,Timer,Cooldown / Hồi chiêu
Grind,Mechanic,Repetitive Work,Cày cuốc
Farm,Mechanic,Resource Gathering,Farm / Cày đồ
Drop Rate,Mechanic,Loot Chance,Tỷ lệ rớt đồ
Vendor Trash,Slang,Useless Items,Rác (Trash)
Wipe,Slang,Party Death,Wipe / Chết sạch
Credit Card Player,Slang,Pay-to-Win (Derogatory),Đô-la Thần Chưởng (Dollar Palm Technique)
Soc / Socs,Slang,Social Gamer (Derogatory),Dân Soc / Dân buôn chuyện
Rper,Slang,Role-player,Dân RP / Diễn sâu
Toxic Muffins,Faction,Guild Name (Juvenile/Edgy),Toxic Muffins (Bánh Muffin Độc)
Elechopper,Item,Magical Motorcycle,Elechopper (Mô-tô Nguyên Tố)
Exsanguinator,Item,Vampiric Sword,Huyết Kiếm (Blood Sword)
Lightning's Bite,Item,Electric Staff,Lôi Nha (Thunder Fang)
Cupcake Keep,Location,Guild Hall,Lâu Đài Cupcake
Dragonsbane,Quest,Legendary Title,Đồ Long (Dragon Slayer)
Hotfix,System,Live Update,Hotfix / Bản vá nóng
Macro,System,Automated Command,Macro / Lệnh tự động
Virtual Tablet (VT),System,Handheld UI,VT / Máy tính bảng ảo
"""

# ==============================================================================
# 3. KINSHIP MAP (Corrected Relationships)
# ==============================================================================
CONTENT_KINSHIP = """[SCHEMA DEFINITION]
Entity_Structure: {ID, Real_Identity, Avatar_Identity, Motivation, Voice_Style, Relations}

[THE TOXIC MUFFINS - CORE]
1. JUSTINE (Protagonist)
   - Avatar: **Melpomine** (Half-Elf) / **Scootiwutams** (Dwarf) / **Stabbies** (Human).
   - Identity: **Jordan's Sister.** Game Dev.
   - Motivation: Honoring her dead brother's legacy. Survival.
   - Voice:
     * *Internal:* Cynical, Grieving, Analytical.
     * *Scooti:* Scottish Stereotype (Rough Dialect).
     * *Melpomine:* Professional Gamer.
   - Relations: Sister to Jordan; "Boss" to the Guild.

2. MIRAE
   - Avatar: **Mirae** (Healer).
   - Identity: Disabled (Wheelchair-bound in reality).
   - Motivation: **Freedom.** She loves the game because she can walk.
   - Voice: Joyful, Enthusiastic, Gamer Savvy.
   - Relations: Flirtatious with TakoStar. Loyal to Justine.

3. TAKOSTAR
   - Avatar: **Tako** (Rogue).
   - Identity: Student (High School/College).
   - Motivation: Fun, Camaraderie.
   - Voice: "Lame Jokes," Pop Culture Refs, Slang.
   - Relations: "Younger Brother" (Em) dynamic with Frobod. Crushing on Mirae.

4. FROBOD
   - Avatar: **Frobod** (Death Knight).
   - Identity: 32-year-old man.
   - Motivation: **Getting back to his DAUGHTER.** (Anxious Father).
   - Voice: Direct, Pragmatic, Serious. NOT a Role-player.
   - Relations: "Older Brother" (Anh) to Tako.

5. LAURELADE
   - Avatar: **Laurelade** (Gnome Mage).
   - Identity: Solo Gamer.
   - Motivation: Effectiveness, Loot, Adventure.
   - Voice: **Low-Energy Bureaucrat / Moody Teen.** ("Whatever", "I don't care").
   - Note: She respects Justine's *results* (Effectiveness), not the "Art" of her build.

[THE TOXIC MUFFINS - EXTENDED FAMILY]
6. PEHROM (The Chef)
   - Identity: Professional Chef (Broken heart in real world).
   - Voice: **Foul-Mouthed.** Gritty. "Upstate New Jersey."
   - Role: Cooks flavorful food (Moral support).
   - Relations: Husband to Lily? Brother to Pahrem.

7. LILY
   - Identity: Pehrom's Wife.
   - Role: Joined with the goblin crew.

8. PAHREM
   - Identity: Pehrom's Sibling.
   - Role: Goblin Healer.

9. THE THIRD GOBLIN
   - Note: (Placeholder for the 3rd goblin mentioned in user notes).

[NPCS & ANTAGONISTS]
1. ARCHANGEL (The God)
   - Voice: Lazy, Condescending, Absolute Power.

2. LORD ZARENTU (The Dragon)
   - Voice: Regal, Prideful. Respects Strength.

3. ALFRED/CUPCAKE (The Butler)
   - Voice: Formal Butler vs Visual Absurdity (Topless Elf).
   - Note: Knows Justine is NOT Jordan.
"""

# ==============================================================================
# 4. STORY BIBLE (The Full "Zero Pruning" Dump)
# ==============================================================================
CONTENT_BIBLE = """# STORY_BIBLE.md
*Reference: Detailed Episode Beats & Plot Context*

**[CHAPTER 1: DESIGN]**
The protagonist, a game developer, works in a virtual space to design a new monster's animations with her AI partner, Sal. She physically acts out the raptor-like motions.
* **System Events:** Uses "Respawn" disc.
* **Emotional Current:** Creative, Professional.

**[CHAPTER 2: IN MEMORY]**
Justine logs into her deceased brother **Jordan's** account ("Stabbies"). She watches his 2-year-old buffs (Enhanced Dexterity/Vitality) tick down. She reads his old guild macros ("R-Twined is a PvP Dick!").
* **Emotional Current:** Somber, Nostalgic. Establishing the "Electronic Shrine."

**[CHAPTER 3: ONE LAST TIME]**
She navigates the empty city of Durolan. She meets Biskon (peaceful Half-Orc). She goes to a pond to let the buffs expire. She is interrupted by Elondriel and LadyPoints, who accuse her of being a "Credit Card Player."
* **Emotional Current:** Melancholy -> Irritation -> Cold Panic (wasting time).

**[CHAPTER 4: NEW RIDE]**
**THE MERGE:** Haven and Freeworld merge. Justine creates "Melpomine." She uses the Alias system to switch to "Scootiwutams" (Dwarf) to bypass Guard reputation. She meets TakoStar. She uses Dev perks to clone Jordan's "Nightmare" mount stats onto 5 "Fire Elechoppers."
* **System Events:** Merge Notification. Alias System. Mount Cloning.
* **Emotional Current:** Shock -> Calculation -> Excitement.

**[CHAPTER 5: THERE BE DRAGONS]**
Justine recruits the guild at the Smiling Otter inn. She reveals her Dev status/LE account. Recruits: Tako (Rogue), Frobod (DK), Mirae (Healer), Laurelade (Mage).
* **Emotional Current:** Social, Leadership.

**[CHAPTER 6: IN THE FOREHEAD]**
First combat at Windroost. Chaos. Tako and Frobod die. Justine struggles to hold Aggro but succeeds.
* **System Events:** "Taunt. Successful." "Congratulations! Point Break!"
* **Emotional Current:** Chaotic -> Triumphant Relief.

**[CHAPTER 7: BOSS FIGHTS]**
They defeat Tilashia, Raika, and Nothgoran. Justine acquires "Lightning's Bite" staff. She decides to build an "Evasive Tank" (Martial Arts).
* **Emotional Current:** Strategic, Focused.

**[CHAPTER 8: HOTFIX]**
**TRAPPED.** The "Log Out" button is disabled. Frobod panics (needs to get back to his **Daughter**). Mirae is calm (she is free from her wheelchair).
* **System Events:** Hotfix applied.
* **Emotional Current:** Dread vs Relief (Mirae).

**[CHAPTER 9: CUPCAKE KEEP]**
They find the Guild Hall. Meet Alfred (Cupcake), the drunk AI Butler. He reveals the "Topless Elf" form.
* **Emotional Current:** Worried, Comedic.

**[CHAPTER 10: ARCHANGEL]**
Archangel announces he is God. "Lazy male voice." Introduces Hunger and Permadeath.
* **Emotional Current:** Shock, Terror.

**[CHAPTER 11: FIRST NIGHT FROM HOME]**
Justine reveals to Alfred that she is Jordan's *sister*. She sleeps in the game.
* **Emotional Current:** Intimate, Somber.

**[CHAPTER 12-15: THE TOURNAMENT]**
* **Ch 12:** Arrive at Dragonswood. Meet Lord Zarentu.
* **Ch 13:** Hunger mechanic (Food is tasteless). Justine bets 1000g on Frobod with Sleeve.
* **Ch 14:** Aztram resizes the Elechopper.
* **Ch 15:** Frobod wins the Joust using the Elechopper's speed. Xephrus cries "Alien Magics." Zarentu humbles Xephrus.
* **Emotional Current:** Mischievous -> Triumphant -> Vindicating.

**[CHAPTER 16-17: SINGLE COMBAT]**
* **Ch 16:** Justine wins duel using "Flow Like Water."
* **Ch 17:** Justine vs Lord Krogen. Krogen calls them "Ants." Justine wins by exploiting his pride.
* **Emotional Current:** Intense, Desperate.

**[CHAPTER 18: THE RUMBLE]**
5v5 Team Battle. Toxic Muffins win using tactics (Kiting + Focus Fire).
* **Emotional Current:** Coordinated.

**[CHAPTER 19: REWARDS]**
Victory Feast. Frobod accidentally stabs Justine (Prank gone wrong). Zarentu grants an Alliance.
* **Emotional Current:** Celebratory -> Diplomatic.

**[CHAPTER 20: RISK AND BURGERS]**
* **The Food:** Pehrom (Goblin Chef) cooks Burgers. They have *Flavor*.
* **The Tragedy:** Mirae disappears. Her name vanishes. She has died in the real world (Life support cut?).
* **The Reaction:** Tako is devastated. The Guild is galvanized.
* **Emotional Current:** Joyful -> Crushing Grief.

**[CHAPTER 21: THE LOST CHAMPION]**
Dungeon dive. Found "Essence of the Lost Champion." Justine takes the Darksteel Chakram.
* **Emotional Current:** Tense -> Renewed Purpose.

**[EPILOGUE: DRAGON SLAYERS]**
They defeat Nothgoran again. Earn "Dragonslayer" title. Dedicate it to Mirae.
* **Emotional Current:** Grim Determination.
"""

# ==============================================================================
# 5. PROGRESS LOG (Empty Template)
# ==============================================================================
CONTENT_PROGRESS = """# PROGRESS_LOG.md
*Agent Processing Log - Do not edit manually except to reset.*

**[SYSTEM STATUS: INITIALIZED]**
**[CURRENT EPISODE: N/A]**
**[LAST CHUNK: None]**

(Agents Mai, Quang, and Elara will append their status here as they process the text.)
"""

# ==============================================================================
# EXECUTION
# ==============================================================================

def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"[CREATED] {path}")

def write_file(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"[GENERATED] {path}")

def main():
    print(f"--- POPULATING PROJECT: {PROJECT_NAME} (V6 - FINAL CORRECTIONS) ---")
    
    # 1. Create Project Directory
    ensure_dir(PROJECT_DIR)

    # 2. Write Context Files
    write_file(os.path.join(PROJECT_DIR, "STYLE_GUIDE.md"), CONTENT_STYLE)
    write_file(os.path.join(PROJECT_DIR, "GLOSSARY.csv"), CONTENT_GLOSSARY)
    write_file(os.path.join(PROJECT_DIR, "MASTER_KINSHIP_MAP.txt"), CONTENT_KINSHIP)
    write_file(os.path.join(PROJECT_DIR, "STORY_BIBLE.md"), CONTENT_BIBLE)
    write_file(os.path.join(PROJECT_DIR, "PROGRESS_LOG.md"), CONTENT_PROGRESS)

    print("--- POPULATION COMPLETE ---")
    print("Frobod's daughter, Laurelade's attitude, and Justine's identity are locked in.")

if __name__ == "__main__":
    main()