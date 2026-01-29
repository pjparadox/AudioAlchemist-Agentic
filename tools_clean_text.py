import re

filepath = "Neon_Veil/Chapter_3.md"

with open(filepath, 'r') as f:
    content = f.read()

# Replace Em Dash with hyphen
content = content.replace("—", "-")

# Remove asterisks but keep the text inside
# We need to be careful not to break the scene separator ***
# Strategy:
# 1. Replace *** with a placeholder marker
# 2. Remove all single *
# 3. Restore placeholder to ***

placeholder = "SCENE_BREAK_MARKER"
content = content.replace("***", placeholder)
content = content.replace("*", "")
content = content.replace(placeholder, "***")

with open(filepath, 'w') as f:
    f.write(content)
