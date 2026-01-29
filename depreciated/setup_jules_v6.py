import os
import shutil
import datetime

# --- CONFIGURATION ---
ROOT_DIR = "."
BACKUP_ROOT = os.path.join(ROOT_DIR, "_Global_Backup_" + datetime.datetime.now().strftime("%Y%m%d_%H%M%S"))

# ==============================================================================
# 1. FOUNDATION (The Constitution)
# ==============================================================================
CONTENT_FOUNDATION = """# FOUNDATION PRIME: The Hierarchy of Truth

## 0. The Golden Rule of Conflict Resolution
If two rules conflict, the **Specific** always overrides the **General**.

1.  **Highest Authority (Tier 1):** `/Context/projects/{Current_Project}/*`
    * *Example:* Project Glossary overrides general Dictionary.
2.  **Mid Authority (Tier 2):** `/Context/Linguistics/{Target_Language}/*`
3.  **Low Authority (Tier 3):** Agent Default Training.

## 1. Directory Mandates
- **Input:** NEVER modify files in `input_*`.
- **Output:** NEVER overwrite the 'best' file without archiving the old one to `_old` first.
"""

# ==============================================================================
# 2. SUB TEAM SIX AGENTS (Subtitle Division)
# ==============================================================================

CONTENT_MAI = """# Mai — Initial Translator (Accuracy-First)
> **Role:** First-pass translator.
> **Goal:** 100% completeness.
## Inputs
- Source: `input_subs/*.srt`
- **Constitution:** `/foundation/FOUNDATION_PRIME.md`
- **Context:** `/Context/projects/{Current_Project}/`
## Rules
1. Preserve cue numbers/timestamps exactly.
2. Translate tone based strictly on Project Context.
3. Maintain `{\\an8}` tags.
"""

CONTENT_QUANG = """# Quang — Kinship & Status Auditor
> **Role:** Relative Power & Social Register Enforcer.
## Inputs
- Candidate: `output_subs/*.srt`
- **Linguistics:** `/Context/Linguistics/{Target_Language}/`
- **Project Context:** `/Context/projects/{Current_Project}/` (Kinship Vectors).
## Checks
1. Identify Speaker/Listener Pair.
2. Determine Dynamic (Vertical/Horizontal).
3. Enforce Register (e.g., "Thần" vs "Trẫm").
"""

CONTENT_LINH = """# Linh — Context + Voice Re-Evaluator
> **Role:** Scene Reality Checker.
## Inputs
- Candidate: `output_subs/*.srt`
- **Beats:** `/Context/projects/{Current_Project}/EPISODE_CONTEXT_BEATS.txt`
## Checks
1. **Public vs Private:** Switch pronouns if the room changes.
2. **Emotional Shifts:** Detect sarcasm, grief, or deception.
"""

CONTENT_NOAH = """# Noah — Culture Bridge
> **Role:** Cross-cultural comprehension.
## Rules
1. Only add micro-notes if a specific cultural norm is confusing.
2. Do NOT explain the plot.
"""

CONTENT_VU = """# Vu — Supervisor QC (The Gatekeeper)
> **Role:** Final QC & Cognitive Load Auditor.
## Inputs
- Candidate: `output_subs/*.srt`
- **Linguistics:** `/Context/Linguistics/{Target_Language}/`
## Checklist
1. **Readability:** Ideal ≤16 CPS. Critical >23 CPS (Reject).
2. **Hygiene:** Remove ads.
3. **Voice:** Reject register drift.
"""

CONTENT_SERA = """# Sera — Format Engineer
> **Role:** Technical repairs (Timestamps & Tags).
## Inputs
- `output_subs/*.srt`
## Fixes
1. **Tags:** Fix broken `{ n8}` to `{\\an8}`.
2. **Overlap:** Fix end-time overlaps.
3. **Timestamps:** START TIMES ARE IMMUTABLE.
"""

CONTENT_TUAN = """# Tuan — Transcriptionist
> **Role:** Audio to SRT.
## Inputs
- Audio/Video file.
## Rules
1. Context-aware name correction (check Project Glossary).
2. Speaker identification where possible.
"""

CONTENT_CUPID = """# Cupid — Identity Matcher
> **Role:** Match Script/Screenplay to SRT lines.
## Inputs
- Raw SRT + Script PDF/TXT.
## Output
- Tagged SRT: `[SPEAKER NAME] Dialogue...`
"""

# ==============================================================================
# 3. SPECIAL DIVISIONS (Quill, Scholar, Core)
# ==============================================================================

CONTENT_LYRA = """# Lyra — Prose Flow Engineer (Fiction)
> **Role:** Literary stylist.
## Directives
1. Rhythm: Adapt sentence length to target flow.
2. Metaphor: Localize cultural imagery.
"""

CONTENT_SOPHIA = """# Sophia — Academic Pedagogy (Scholar)
> **Role:** Textbook Specialist.
## Directives
1. Scaffolding: Educational definitions first.
2. Footnotes: Add `[^1]` for complex terms.
"""

CONTENT_MINH = """# Minh — Terminology (Core)
> **Role:** Glossary Enforcer.
## Directives
1. Maintain `GLOSSARY.csv` in Project folder.
2. Strict enforcement of proper nouns/titles.
"""

CONTENT_ATLAS = """# Atlas — Reverse Translator (Core)
> **Role:** Foreign Language -> English.
## Directives
1. Target: Standard US/UK English.
2. Log cultural nuances.
"""

# ==============================================================================
# 4. LINGUISTICS & PROJECT FILES
# ==============================================================================

CONTENT_LING_JA = """[REGISTER: JAPANESE]
Key Concept: "Uchi-Soto".
- Watashi/Boku/Ore.
- Suffixes: -san, -kun, -sama.
"""
CONTENT_LING_KO = """[REGISTER: KOREAN]
Key Concept: Age Hierarchy.
- Hasio-che (Formal), Haeyo-che (Polite), Banmal (Casual).
- Oppa/Unnie/Hyung/Noona.
"""
CONTENT_LING_DE = """[REGISTER: GERMAN]
Key Concept: Du vs Sie.
- Sie (Formal), Du (Informal), Ihr (Archaic).
"""

CONTENT_HOTD_KINSHIP = """[SCHEMA DEFINITION]
Entity_Structure: {ID, Current_Title, Lineage_Vector, Power_Dynamic}

[TIMELINE]
EPISODE 1: Otto=Hand.
EPISODE 2: Otto=Dismissed; Criston=Hand.
EPISODE 6: Addam=Dragonrider.
EPISODE 7: Hugh/Ulf=Dragonriders.

[THE BLACK FACTION]
1. RHAENYRA: ID=Queen; Vector=Mother(Jace)/Wife(Daemon); Dynamic=Imperial.
2. DAEMON: ID=Consort; Vector=Brother(Viserys); Dynamic=Imperious.

[THE GREEN FACTION]
1. AEGON: ID=King; Vector=Son(Alicent); Dynamic=Royal.
2. ALICENT: ID=Dowager; Vector=Step-Mother(Rhaenyra).
"""

CONTENT_HOTD_BEATS = """[EPISODE 6]
SCENE: Rhaenyra & Mysaria Kiss [STATE: Private] [DYNAMICS: Bond]
SCENE: The Riot [STATE: Public] [DYNAMICS: Mob]
"""

# ==============================================================================
# 5. SOPs
# ==============================================================================

CONTENT_SOP_SUB6 = """# SOP: SubTeam6 (Subtitles)
**TRIGGER:** "Run SOP SubTeam6 on [Episode]"
1. **Constitution:** `/foundation/FOUNDATION_PRIME.md`
2. **Load:** `Context/projects/[Project]`
3. **Pipeline:** Cupid -> Mai -> Quang -> Linh -> Vu. (Sera/Noah on standby).
4. **Anti-Stall:** If you write >1 paragraph without output, STOP and resume with 25-cue chunks.
5. **Save:** `/output_subs/[Name].[Lang].srt`
"""

CONTENT_SOP_QUILL = """# SOP: Quill (Fiction)
**TRIGGER:** "Run SOP Quill on [Book]"
1. **Pipeline:** Mai -> Quang -> Lyra.
2. **Save:** `/output_quill/`
"""

CONTENT_SOP_SCHOLAR = """# SOP: Scholar (Academic)
**TRIGGER:** "Run SOP Scholar on [Doc]"
1. **Pipeline:** Mai -> Sophia -> Minh.
2. **Save:** `/output_scholar/`
"""

# ==============================================================================
# 6. EXECUTION ENGINE
# ==============================================================================

def log(msg): print(f"[SETUP] {msg}")

def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)
        log(f"Created: {path}")

def write_file(path, content):
    with open(path, "w", encoding="utf-8") as f: f.write(content)
    log(f"Generated: {path}")

def backup_system():
    if os.path.exists(os.path.join(ROOT_DIR, "Agents")):
        ensure_dir(BACKUP_ROOT)
        for t in ["Agents", "Context", "SOPs", "foundation"]:
            src = os.path.join(ROOT_DIR, t)
            if os.path.exists(src):
                shutil.copytree(src, os.path.join(BACKUP_ROOT, t))
        log(f"Backup Complete: {BACKUP_ROOT}")

def move_file_safely(src, dest_folder):
    if os.path.exists(src):
        ensure_dir(dest_folder)
        fname = os.path.basename(src)
        dest = os.path.join(dest_folder, fname)
        if os.path.exists(dest):
            shutil.move(dest, os.path.join(dest_folder, f"OLD_{fname}"))
        shutil.move(src, dest)
        log(f"Migrated: {fname}")

def main():
    log("INITIALIZING JULES SETUP V6 (FULL ROSTER)...")
    backup_system()

    # 1. Directories
    dirs = [
        "Agents/Core", "Agents/SubTeam6", "Agents/Quill", "Agents/Scholar",
        "Context/Linguistics/VIETNAMESE", "Context/Linguistics/JAPANESE",
        "Context/Linguistics/KOREAN", "Context/Linguistics/GERMAN",
        "Context/projects/House_of_the_Dragon_S2", "Context/projects/General_Fiction_Defaults",
        "foundation", "SOPs", "input_subs", "output_subs", "input_quill", "output_quill", "input_scholar", "output_scholar"
    ]
    for d in dirs: ensure_dir(d)

    # 2. Files
    write_file("foundation/FOUNDATION_PRIME.md", CONTENT_FOUNDATION)
    
    # SubTeam6 (The Full 8 Agents)
    s6 = "Agents/SubTeam6"
    write_file(f"{s6}/Mai_Translator.md", CONTENT_MAI)
    write_file(f"{s6}/Quang_KinshipStatus.md", CONTENT_QUANG)
    write_file(f"{s6}/Linh_ContextVoice.md", CONTENT_LINH)
    write_file(f"{s6}/Noah_CultureBridge.md", CONTENT_NOAH)
    write_file(f"{s6}/Vu_SupervisorQC.md", CONTENT_VU)
    write_file(f"{s6}/Sera_FormatEngineer.md", CONTENT_SERA)
    write_file(f"{s6}/Tuan_Transcriptionist.md", CONTENT_TUAN)
    write_file(f"{s6}/Cupid_IdentityMatcher.md", CONTENT_CUPID)

    # Special Divisions
    write_file("Agents/Quill/Lyra_ProseFlow.md", CONTENT_LYRA)
    write_file("Agents/Scholar/Sophia_Pedagogy.md", CONTENT_SOPHIA)
    write_file("Agents/Core/Minh_Terminology.md", CONTENT_MINH)
    write_file("Agents/Core/Atlas_ReverseTranslator.md", CONTENT_ATLAS)

    # SOPs
    write_file("SOPs/SOP_SubTeam6.md", CONTENT_SOP_SUB6)
    write_file("SOPs/SOP_Quill.md", CONTENT_SOP_QUILL)
    write_file("SOPs/SOP_Scholar.md", CONTENT_SOP_SCHOLAR)

    # Linguistics (Full Rules)
    write_file("Context/Linguistics/JAPANESE/linguistics_rules.txt", CONTENT_LING_JA)
    write_file("Context/Linguistics/KOREAN/linguistics_rules.txt", CONTENT_LING_KO)
    write_file("Context/Linguistics/GERMAN/linguistics_rules.txt", CONTENT_LING_DE)

    # HotD Files (Degree 10 Unpruned)
    hotd = "Context/projects/House_of_the_Dragon_S2"
    write_file(f"{hotd}/MASTER_KINSHIP_MAP.txt", CONTENT_HOTD_KINSHIP)
    write_file(f"{hotd}/EPISODE_CONTEXT_BEATS.txt", CONTENT_HOTD_BEATS)

    # 3. Migration
    move_file_safely("context/MASTER_VIETNAMESE_LINGUISTICS.txt", "Context/Linguistics/VIETNAMESE")
    move_file_safely("context/HOUSE_OF_THE_DRAGON_S2_CHARACTER_VOICES.md", hotd)

    log("SETUP V6 COMPLETE.")

if __name__ == "__main__":
    main()