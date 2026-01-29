import os
import re
import datetime

def extract_summary(filepath):
    """Extracts a brief summary from the agent/file content."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            # Look for lines starting with "Role:" or "Purpose:"
            match = re.search(r'^(Role|Purpose|Goal):\s*(.+)$', content, re.MULTILINE)
            if match:
                return match.group(2).strip()
            # Fallback to first non-header line
            lines = content.split('\n')
            for line in lines:
                if line.strip() and not line.startswith('#'):
                    return line.strip()[:100] + "..."
    except Exception:
        return "No summary available."
    return "No summary available."

def get_team_description(dirname):
    """Returns a description for a given team directory."""
    descriptions = {
        "Argus": "Research & Intelligence",
        "Caduceus": "Medical Division",
        "Core": "Core Utilities",
        "Gavel": "Legal Division",
        "Grigori": "System Integrity & Enforcement",
        "HeartHome": "Heart & Home (Emotional Intelligence & Communications)",
        "Hephaestus": "Manuscript Revision & Reforging",
        "Oversight": "Internal Affairs & Governance",
        "Quill": "Fiction/Literary Specialists",
        "Scholar": "Academic/Pedagogical Specialists",
        "Scribes": "Franchise & Canon Specialists (Scribes of Old Valyria)",
        "SubTeam6": "Subtitle Specialists",
        "Veil": "Specialized Safety & Accessibility (The Veil)",
        "Utilities": "General Utilities"
    }
    return descriptions.get(dirname, "Specialized Agent Team")

def rebuild_archive():
    # Assuming script is run from project root
    archive_path = "MASTER_SUITE_ARCHIVE.txt"

    # 1. ROOT FILES
    root_files = ["AGENTS.md", "PROCESSING_PROTOCOL.md", "README.md", "CHANGELOG.md", "SESSION_INIT.md"]

    # 2. SYSTEM DIRECTORIES
    system_dirs = ["Agents", "SOPs", "foundation", "prompts"]

    # 3. CONTEXT (Selective)
    context_whitelist = [os.path.join("context", "global"), os.path.join("context", "templates")]

    # 4. SCRIPTS
    scripts_dir = "foundation/approved_scripts"

    # --- DATA COLLECTION ---
    teams_data = {} # {team_name: {desc, agents: [{name, summary, path}]}}
    guidelines_data = [] # [{name, summary, path}]
    scripts_data = []
    global_context_data = []

    # Collect Teams & Agents
    if os.path.exists("Agents"):
        for item in sorted(os.listdir("Agents")):
            item_path = os.path.join("Agents", item)
            if os.path.isdir(item_path) and not item.startswith('.'):
                team_name = item
                team_desc = get_team_description(team_name)
                agents = []
                for root, dirs, files in os.walk(item_path):
                    for file in sorted(files):
                        if file.endswith(".md") or file.endswith(".txt"):
                            fpath = os.path.join(root, file)
                            summary = extract_summary(fpath)
                            agents.append({"name": file, "summary": summary, "path": fpath})
                teams_data[team_name] = {"description": team_desc, "agents": agents}

    # Collect Guidelines (SOPs, Root, Foundation)
    # Root
    for f in root_files:
        if os.path.exists(f):
            summary = extract_summary(f)
            guidelines_data.append({"name": f, "summary": summary, "path": f, "type": "Root Protocol"})

    # SOPs
    if os.path.exists("SOPs"):
        for root, dirs, files in os.walk("SOPs"):
            for file in sorted(files):
                 if file.endswith(".md") or file.endswith(".txt"):
                    fpath = os.path.join(root, file)
                    summary = extract_summary(fpath)
                    guidelines_data.append({"name": file, "summary": summary, "path": fpath, "type": "Standard Operating Procedure"})

    # Foundation
    if os.path.exists("foundation"):
        for root, dirs, files in os.walk("foundation"):
            if "approved_scripts" in root: continue # Skip scripts here
            for file in sorted(files):
                 if file.endswith(".md") or file.endswith(".txt"):
                    fpath = os.path.join(root, file)
                    summary = extract_summary(fpath)
                    guidelines_data.append({"name": file, "summary": summary, "path": fpath, "type": "Foundation Mandate"})

    # Collect Scripts
    if os.path.exists(scripts_dir):
        for file in sorted(os.listdir(scripts_dir)):
            if file.endswith(".py"):
                fpath = os.path.join(scripts_dir, file)
                scripts_data.append({"name": file, "path": fpath})

    # Collect Global Context
    for d in context_whitelist:
        if os.path.exists(d):
            for root, dirs, files in os.walk(d):
                for file in sorted(files):
                     if file.endswith(".md") or file.endswith(".txt"):
                        fpath = os.path.join(root, file)
                        summary = extract_summary(fpath)
                        global_context_data.append({"name": file, "summary": summary, "path": fpath})


    # --- WRITE ARCHIVE ---
    with open(archive_path, 'w', encoding='utf-8') as outfile:
        outfile.write("# MASTER SUITE ARCHIVE\n")
        outfile.write(f"# Generated by Metatron on {os.environ.get('JULES_SESSION_ID', 'Unknown Session')} / {datetime.datetime.now().isoformat()}\n")
        outfile.write("# SCOPE: Active Agents, Protocols, SOPs, and System-Level Context. Project Data Excluded.\n\n")

        # --- SECTION 1: SYSTEM MANIFEST ---
        outfile.write("## 1. SYSTEM DIRECTORY & MANIFEST\n\n")

        outfile.write("### A. TEAMS & AGENTS\n")
        for team_name, data in sorted(teams_data.items()):
            outfile.write(f"- **{team_name}** ({data['description']})\n")
            for agent in data['agents']:
                outfile.write(f"  - `{agent['name']}`: {agent['summary']}\n")
            outfile.write("\n")

        outfile.write("### B. PROTOCOLS & MANDATES\n")
        for item in guidelines_data:
            outfile.write(f"- **{item['name']}** ({item['type']}): {item['summary']}\n")
        outfile.write("\n")

        outfile.write("### C. APPROVED SCRIPTS\n")
        for item in scripts_data:
            outfile.write(f"- `{item['name']}`\n")
        outfile.write("\n\n")


        # --- SECTION 2: FULL TEXT ARCHIVE ---
        outfile.write("## 2. FULL TEXT ARCHIVE\n\n")

        # 2.1 Root & Guidelines
        outfile.write("### 2.1 ROOT PROTOCOLS & MANDATES\n\n")
        for item in guidelines_data:
             outfile.write(f"--- FILE: {item['path']} ({item['summary']}) ---\n")
             with open(item['path'], 'r', encoding='utf-8') as infile:
                 outfile.write(infile.read())
             outfile.write("\n\n\n")

        # 2.2 Agents
        outfile.write("### 2.2 AGENTS\n\n")
        for team_name, data in sorted(teams_data.items()):
            outfile.write(f"#### TEAM: {team_name} ({data['description']})\n")
            for agent in data['agents']:
                outfile.write(f"--- FILE: {agent['path']} ({agent['summary']}) ---\n")
                with open(agent['path'], 'r', encoding='utf-8') as infile:
                    outfile.write(infile.read())
                outfile.write("\n\n\n")

        # 2.3 Scripts
        outfile.write("### 2.3 APPROVED SCRIPTS\n\n")
        for item in scripts_data:
            outfile.write(f"--- SCRIPT: {item['path']} ---\n")
            with open(item['path'], 'r', encoding='utf-8') as infile:
                outfile.write(infile.read())
            outfile.write("\n\n\n")

        # 2.4 Global Context
        outfile.write("### 2.4 GLOBAL CONTEXT\n\n")
        for item in global_context_data:
            outfile.write(f"--- FILE: {item['path']} ({item['summary']}) ---\n")
            with open(item['path'], 'r', encoding='utf-8') as infile:
                outfile.write(infile.read())
            outfile.write("\n\n\n")

    print(f"Archive successfully rebuilt at {archive_path}")

if __name__ == "__main__":
    rebuild_archive()
