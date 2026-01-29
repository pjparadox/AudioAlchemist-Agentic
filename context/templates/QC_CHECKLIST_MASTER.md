# MASTER QC CHECKLIST (MQM-Lite)
*Copy and paste this into your ADVERSARIAL_LOG or PROJECT_LOG for every audit pass.*

**Agent:** [Name]
**Project:** [Project Name]
**Pass Type:** [e.g., Initial Draft, Final Polish, 14th Degree Audit]

## 1. ACCURACY & MEANING (The "Truth" Check)
- [ ] **Reverse Translation Check:** Did I mentally translate the VN back to EN? Does it match the source intent?
- [ ] **Omission Check:** Are any critical plot points or jokes missing?
- [ ] **Hallucination Check:** Did the model invent details not in the source?

## 2. FLUENCY & NATURALNESS (The "Ear" Check)
- [ ] **Read Aloud Test:** Does this sentence sound like a real Vietnamese person speaking, or "Google Translate"?
- [ ] **Idiom Audit:** Are English idioms (e.g., "piece of cake") translated to Vietnamese equivalents ("dễ như ăn kẹo") rather than literal nonsense?
- [ ] **Grammar:** Is the syntax perfect?

## 3. TERMINOLOGY & KINSHIP (The "Consistency" Check)
- [ ] **Kinship Graph:** Are pronouns (Anh/Em/Tao/Mày/Cháu/Bà) consistent with the `RELATIONSHIP_MATRIX`?
- [ ] **Glossary:** Are all proper nouns and technical terms (e.g., "Ice Box", "X-Force") handled according to the Project Glossary?

## 4. TONE & REGISTER (The "Voice" Check)
- [ ] **Profanity Tier:** Does the vulgarity match the source? (e.g., "Fuck" -> "Đụ má" / "Shit" -> "Chết tiệt").
- [ ] **Character Voice:** Does the lawyer sound like a lawyer? Does the gangster sound like a gangster?

## 5. SUBTITLE ENGINEERING (The "Viewer" Check) - *Subtitle Projects Only*
- [ ] **Start Times:** Confirmed IMMUTABLE (Matched source exactly).
- [ ] **End Times:** Extended where safe (non-overlapping) to improve reading speed?
- [ ] **CPS Check:** Is the line under 20 CPS (Adults) / 17 CPS (Kids)?
- [ ] **Condensation:** If CPS is high, was the line **Rewritten/Condensed** rather than just translated literally?
- [ ] **Formatting:** No duplicate lines? No foreign text bloat (unless atmospheric)?

## 6. CULTURAL NUANCE (The "Depth" Check)
- [ ] **Localization:** Are cultural references (e.g., politicians, TV shows) handled effectively (either adapted or annotated with 'Noah's Notation')?
- [ ] **Political Awareness:** Is the political satire preserved?

**VERDICT:** [PASS / FAIL / REVISE]
**SCORE:** [0-10]
