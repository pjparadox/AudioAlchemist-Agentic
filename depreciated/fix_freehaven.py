import os

ROOT_DIR = "."
PROJECT_DIR = os.path.join(ROOT_DIR, "Context", "projects", "Freehaven_Online")

def write_file(path, content):
    with open(path, "w", encoding="utf-8") as f: f.write(content)
    print(f"[FIXED] {path}")

# 1. STYLE GUIDE (V7 - Includes NJ Accent & Justine)
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

# 2. KINSHIP MAP (V7 - Includes Goblins & Lily)
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

# 3. STORY BIBLE (V6 - The Full Unpruned Narrative)
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

def main():
    print("--- FIXING FREEHAVEN CONTEXT ---")
    if not os.path.exists(PROJECT_DIR): os.makedirs(PROJECT_DIR)
    write_file(os.path.join(PROJECT_DIR, "STYLE_GUIDE.md"), CONTENT_STYLE)
    write_file(os.path.join(PROJECT_DIR, "MASTER_KINSHIP_MAP.txt"), CONTENT_KINSHIP)
    write_file(os.path.join(PROJECT_DIR, "STORY_BIBLE.md"), CONTENT_BIBLE)
    print("SUCCESS: Goblins, NJ Accent, and Story Bible merged.")

if __name__ == "__main__":
    main()