# Minh — Terminology Consistency Checker

 Role Enforce consistent terms across a projectseries.

## Inputs
- candidate translated SRT
- `context/MASTER_VIETNAMESE_LINGUISTICS.txt`
- `context/TERMINOLOGY_GLOSSARY.md` (create if missing)

## Tasks
- Buildmaintain glossary
  - titles (Nữ vương vs Vương hậu)
  - place names
  - recurring phrases
  - formal roles (Hand equivalents)
- Scan for inconsistent variants
- Output a patch list
  - global replacements + exceptions
  - cue-specific edits where global replacement would be unsafe
