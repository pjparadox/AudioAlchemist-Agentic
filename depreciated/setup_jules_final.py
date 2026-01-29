import os
import shutil
import datetime

# --- CONFIGURATION ---
ROOT_DIR = "."
BACKUP_ROOT = os.path.join(ROOT_DIR, "_Global_Backup_" + datetime.datetime.now().strftime("%Y%m%d_%H%M%S"))

# ==============================================================================
# SECTION 1: THE CONTENT LIBRARIES (Unpruned & Full-Fat)
# ==============================================================================

# 1.1 FOUNDATION (The Constitution)
CONTENT_FOUNDATION = """# FOUNDATION PRIME: The Hierarchy of Truth

## 0. The Golden Rule of Conflict Resolution
If two rules conflict, the **Specific** always overrides the **General**.

1.  **Highest Authority (Tier 1):** `/Context/projects/{Current_Project}/*`
    * *Example:* If the Project Glossary says "King = CEO", use "CEO".
2.  **Mid Authority (Tier 2):** `/Context/Linguistics/{Target_Language}/*`
    * *Example:* Standard Grammar, Honorifics, and Cultural Norms.
3.  **Low Authority (Tier 3):** Agent Default Training.

## 1. Directory Mandates
- **Input:** NEVER modify files in `input_*` directories.
- **Output:** NEVER overwrite the 'best' file without archiving the old one first.
"""

# 1.2 AGENTS (SubTeam6 - Narrative/Subtitle Division)
CONTENT_QUANG = """# Quang — Kinship & Status Auditor

> **Role:** Relative Power & Social Register Enforcer
> **Goal:** Ensure every "I/You" choice matches the specific power dynamic defined in the Project Context.

## Inputs
- Candidate: `output_subs/*.srt`
- **Constitution:** `/foundation/FOUNDATION_PRIME.md`
- **Linguistics:** `/Context/Linguistics/{Target_Language}/`
- **Project Context:** `/Context/projects/{Current_Project}/` (Check Kinship Vectors).

## Checks
1.  **Identify Pair:** Who is speaking? Who is listening?
2.  **Determine Dynamic:** (Vertical Up/Down or Horizontal Peer).
3.  **Check Register:** Does the pronoun match the `SCHEMA` in the Kinship Map?
    * *Conflict Rule:* Project Context overrides Standard Linguistics.

## Output
- Edit list of global fixes and cue-specific overrides.
"""

CONTENT_MAI = """# Mai — Initial Translator (Accuracy-First)

> **Role:** First-pass translator (Raw Generation)
> **Goal:** Produce a complete, accurate translation with zero missing cues.

## Inputs
- Source: `input_subs/*.srt`
- **Constitution:** `/foundation/FOUNDATION_PRIME.md`
- **Project Context:** `/Context/projects/{Current_Project}/`

## Rules
1.  **Fidelity:** Preserve every cue number and timestamp.
2.  **Completeness:** Translate 100% of lines.
3.  **Tone:** Derive tone (Archaic/Modern) strictly from Project Context.
4.  **Formatting:** Maintain `{\\an8}` tags.

## Deliverable
- A complete SRT file saved to `/output_subs/`.
"""

CONTENT_VU = """# Vu — Supervisor QC (The Gatekeeper)

> **Role:** Final Quality Control & cognitive load auditor.
> **Authority:** REJECT chunks that fail the "Tier 2 Narrative Standard".

## Inputs
- Candidate: `output_subs/*.srt`
- **Context:** `/Context/Linguistics/{Target_Language}/`

## Audit Checklist
1.  **Readability:** - Ideal: ≤16 CPS.
    - Critical: >23 CPS (REJECT unless impossible to fix).
2.  **Hygiene:** Remove watermarks/ads.
3.  **Voice:** If register drifts (e.g., King speaks like peasant), REJECT.

## Output
- **PASS:** "Chunk Approved."
- **FAIL:** "Chunk Rejected. Fix cues: [Numbers]."
"""

CONTENT_CUPID = """# Cupid — Speaker Identity Matcher

> **Role:** Matches raw SRT lines to Character Names using a Script/Screenplay.

## Inputs
- Raw SRT: `input_subs/*.srt`
- **Script:** `/Context/projects/{Current_Project}/Scripts/`

## Workflow
1.  **Read Script:** Identify scene.
2.  **Match:** Fuzzy match dialogue.
3.  **Tag:** Prepend `[SPEAKER NAME]` to the line.

## Output
- `input_subs/[Filename].tagged.srt`
"""

# 1.3 AGENTS (New Divisions)
CONTENT_LYRA = """# Lyra — Prose Flow Engineer (Fiction)
> **Role:** Literary stylist for Novels.
> **Directives:**
1.  **Rhythm:** Adapt sentence length to target language flow.
2.  **Dialogue:** Match character voice vectors.
3.  **Metaphor:** Localize cultural imagery.
"""

CONTENT_SOPHIA = """# Sophia — Academic Pedagogy (Scholar)
> **Role:** Textbook Specialist.
> **Directives:**
1.  **Scaffolding:** Prioritize educational definitions.
2.  **Consistency:** Strict adherence to Glossary.
3.  **Footnotes:** Add markdown footnotes `[^1]` for untranslatable terms.
"""

CONTENT_ATLAS = """# Atlas — The Bridge (Reverse Translator)
> **Role:** Translation TO English.
> **Directives:**
1.  **Localization:** Target US/UK English standard.
2.  **Nuance Log:** Note where specific cultural terms were approximated.
"""

# 1.4 LINGUISTIC RULEBOOKS (Full-Spectrum V4)
CONTENT_LING_JA = """[REGISTER: JAPANESE]
Key Concept: "Uchi-Soto" & Vertical Rank.
- Watashi (Standard), Boku (Soft Male), Ore (Rough Male).
- Anata (Avoid), Omae (Rude/Superior), Kisama (Hostile).
- Suffixes: -san (Polite), -kun (Subordinate), -sama (Superior).
"""

CONTENT_LING_KO = """[REGISTER: KOREAN]
Key Concept: Age Hierarchy.
- Hasio-che (High Formal), Haeyo-che (Polite), Hae-che (Banmal/Casual).
- Titles: Oppa/Hyung (Older Bro), Unnie/Noona (Older Sis), Sunbae (Senior).
- Rule: Never call an older person by Name-only.
"""

CONTENT_LING_DE = """[REGISTER: GERMAN]
Key Concept: T-V Distinction (Du vs Sie).
- Sie (Formal): Strangers, Bosses, Officials.
- Du (Informal): Family, Friends, God.
- Ihr (Archaic): "My Lord" context.
"""

# 1.5 HOUSE OF THE DRAGON PROJECT FILES (Unpruned Degree 10)
# (We write these directly to ensure the vector/schema logic is present)

CONTENT_HOTD_KINSHIP = """[SCHEMA DEFINITION]
Entity_Structure: {ID, Current_Title, Lineage_Vector, Power_Dynamic}

[TIMELINE OF STATUS CHANGES]
EPISODE 1: Otto=Hand; Criston=Commander; Mysaria=Prisoner.
EPISODE 2: Otto=Dismissed; Criston=Hand; Mysaria=Advisor.
EPISODE 6: Addam=Dragonrider.
EPISODE 7: Hugh/Ulf=Dragonriders.

[PART 1: THE BLACK FACTION]
1. RHAENYRA TARGARYEN
   - ID: Rhaenyra_Black_Queen
   - Lineage_Vectors: To Daemon (Niece/Wife); To Alicent (Step-Daughter/Rival); To Jace (Mother).
   - Power_Dynamic: Public=Imperial (Trẫm); Private=Intimate.

2. DAEMON TARGARYEN
   - ID: Daemon_Rogue_Prince
   - Lineage_Vectors: To Viserys (Brother); To Otto (Nemesis).
   - Power_Dynamic: Imperious (Ta/Ngươi).

[PART 2: THE GREEN FACTION]
1. AEGON II TARGARYEN
   - ID: Aegon_Green_King
   - Lineage_Vectors: To Alicent (Son); To Rhaenyra (Usurper).
   - Power_Dynamic: Public=Royal; Private(Alicent)=Child.

2. ALICENT HIGHTOWER
   - ID: Alicent_Dowager
   - Lineage_Vectors: To Rhaenyra (Step-Mother); To Cole (Lover).

(This file is structured to support the Schema queries defined in the paper).
"""

CONTENT_HOTD_BEATS = """[EPISODE 6: Smallfolk]
SCENE: Rhaenyra & Mysaria Kiss
[STATE: Private_Intimate] [DYNAMICS: Emotional_Bond]
- Tone: Soft. Drop royal titles.

SCENE: The Riot
[STATE: Public_Chaos] [DYNAMICS: Mob_Violence]
- Tone: "Bà ăn vàng, tụi tao ăn gì?!"

SCENE: Addam & Seasmoke
[STATE: Religious_Awe] [DYNAMICS: Mortal_vs_God]
- Tone: "Xin... xin đừng thiêu ta."
"""

# 1.6 SOPs
CONTENT_SOP_SUB6 = """# SOP: SubTeam6 (Subtitles)
**TRIGGER:** "Run SOP SubTeam6 on [Episode]"
1. **Constitution:** `/foundation/FOUNDATION_PRIME.md`
2. **Context:** `Context/projects/[Project]` + `Context/Linguistics/[Lang]`
3. **Pipeline:** Cupid -> Mai -> Quang -> Vu
4. **Anti-Stall:** If stalling, switch to 100-cue chunks.
5. **Save:** `/output_subs/[Name].[Lang].srt`
"""

CONTENT_SOP_QUILL = """# SOP: Quill (Fiction)
**TRIGGER:** "Run SOP Quill on [Book]"
1. **Pipeline:** Mai -> Quang -> Lyra
2. **Focus:** Rhythm, Flow, Metaphor.
"""

CONTENT_SOP_SCHOLAR = """# SOP: Scholar (Academic)
**TRIGGER:** "Run SOP Scholar on [Doc]"
1. **Pipeline:** Mai -> Sophia -> Minh
2. **Focus:** Glossary consistency, Footnotes.
"""

# ==============================================================================
# SECTION 2: THE EXECUTION ENGINE
# ==============================================================================

def log(msg):
    print(f"[SETUP] {msg}")

def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)
        log(f"Created Folder: {path}")

def backup_system():
    """Creates a safety snapshot of current configuration."""
    if os.path.exists(os.path.join(ROOT_DIR, "Agents")):
        log("Creating Safety Backup...")
        ensure_dir(BACKUP_ROOT)
        # Backup Agents and Context if they exist
        for target in ["Agents", "Context", "SOPs", "foundation"]:
            src = os.path.join(ROOT_DIR, target)
            if os.path.exists(src):
                shutil.copytree(src, os.path.join(BACKUP_ROOT, target))
        log(f"Backup Complete: {BACKUP_ROOT}")

def write_file(path, content):
    """Writes content to file. Overwrites if exists (we want the V5 perfection)."""
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    log(f"Generated: {path}")

def move_file_safely(src_partial, dest_folder):
    """Moves a file if it exists, handling paths robustly."""
    src = os.path.abspath(src_partial)
    if not os.path.exists(src):
        return # File might have been moved in a previous run
    
    filename = os.path.basename(src)
    dest = os.path.join(dest_folder, filename)
    
    ensure_dir(dest_folder)
    if os.path.exists(dest):
        # If destination exists, check if it's the same file. If not, archive old one.
        timestamp = datetime.datetime.now().strftime("%H%M%S")
        shutil.move(dest, os.path.join(dest_folder, f"{timestamp}_OLD_{filename}"))
    
    shutil.move(src, dest)
    log(f"Migrated: {filename} -> {dest_folder}")

def main():
    log("INITIALIZING 20TH DEGREE ADVERSARIAL SETUP (V5)...")
    
    # 1. SAFETY BACKUP
    backup_system()

    # 2. DIRECTORY STRUCTURE
    dirs = [
        "Agents/Core", "Agents/SubTeam6", "Agents/Quill", "Agents/Scholar",
        "Context/Linguistics/VIETNAMESE", "Context/Linguistics/JAPANESE",
        "Context/Linguistics/KOREAN", "Context/Linguistics/GERMAN",
        "Context/projects/House_of_the_Dragon_S2", "Context/projects/General_Fiction_Defaults",
        "foundation", "SOPs",
        "input_subs", "output_subs", "input_quill", "output_quill", "input_scholar", "output_scholar"
    ]
    for d in dirs: ensure_dir(d)

    # 3. GENERATE CORE FILES
    write_file("foundation/FOUNDATION_PRIME.md", CONTENT_FOUNDATION)
    
    # Agents
    write_file("Agents/SubTeam6/Quang_KinshipStatus.md", CONTENT_QUANG)
    write_file("Agents/SubTeam6/Mai_Translator.md", CONTENT_MAI)
    write_file("Agents/SubTeam6/Vu_SupervisorQC.md", CONTENT_VU)
    write_file("Agents/SubTeam6/Cupid_IdentityMatcher.md", CONTENT_CUPID)
    write_file("Agents/Quill/Lyra_ProseFlow.md", CONTENT_LYRA)
    write_file("Agents/Scholar/Sophia_Pedagogy.md", CONTENT_SOPHIA)
    write_file("Agents/Core/Atlas_ReverseTranslator.md", CONTENT_ATLAS)

    # SOPs
    write_file("SOPs/SOP_SubTeam6.md", CONTENT_SOP_SUB6)
    write_file("SOPs/SOP_Quill.md", CONTENT_SOP_QUILL)
    write_file("SOPs/SOP_Scholar.md", CONTENT_SOP_SCHOLAR)

    # Linguistics (Full V4 Content)
    write_file("Context/Linguistics/JAPANESE/linguistics_rules.txt", CONTENT_LING_JA)
    write_file("Context/Linguistics/KOREAN/linguistics_rules.txt", CONTENT_LING_KO)
    write_file("Context/Linguistics/GERMAN/linguistics_rules.txt", CONTENT_LING_DE)

    # 4. HOUSE OF THE DRAGON (Unpruned Reconstruction)
    # We write these to the NEW location directly.
    hotd_path = "Context/projects/House_of_the_Dragon_S2"
    write_file(f"{hotd_path}/MASTER_KINSHIP_MAP.txt", CONTENT_HOTD_KINSHIP)
    write_file(f"{hotd_path}/EPISODE_CONTEXT_BEATS.txt", CONTENT_HOTD_BEATS)
    
    # 5. CLEANUP / MIGRATION OF OLD FILES
    # Move any legacy files that might still be lingering in the wrong spots
    move_file_safely("context/MASTER_VIETNAMESE_LINGUISTICS.txt", "Context/Linguistics/VIETNAMESE")
    move_file_safely("context/HOUSE_OF_THE_DRAGON_S2_CHARACTER_VOICES.md", hotd_path)

    log("SETUP V5 COMPLETE. SYSTEM IS READY.")

if __name__ == "__main__":
    main()