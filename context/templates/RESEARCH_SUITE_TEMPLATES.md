# ARGUS RESEARCH SUITE TEMPLATES

## 1. Provenance Card (Mandatory per Source)
Every accepted source must use this exact block.

```markdown
### Source ID: [S-###]
*   **Title:** [Original Title]
*   **Author/Institution:** [Name]
*   **Date:** [YYYY-MM-DD]
*   **Language:** [Language Code, e.g., EN, VN, DE]
*   **Host Domain:** [e.g., court.gov, nytimes.com]
*   **Reliability Tier:** [Tier 1/2/3/4]
*   **Type:** [PDF/Article/Statute/etc.]
*   **Content Summary:** [1 sentence description]
*   **Supports Claim(s):**
    *   [Claim 1]
    *   [Claim 2]
*   **Reliability Notes:** [Bias, reconstruction, translation issues, etc.]
*   **URL:** [Link]
*   **Access Date:** [YYYY-MM-DD]
```

## 2. Disagreement Box (Mandatory for Conflicts)
Use this when two sources disagree on facts, dates, or interpretations.

```markdown
### ⚠️ DISAGREEMENT: [Subject of Dispute]
| Field | Source A ([ID]) | Source B ([ID]) |
| :--- | :--- | :--- |
| **Claim** | "[Quote A]" | "[Quote B]" |
| **Date/Value** | [Value A] | [Value B] |
| **Context** | [Context A] | [Context B] |

*   **Analysis:** [Why does this disagreement exist? e.g., Different methodologies, updated info.]
*   **Resolution Strategy:** [What evidence is needed to resolve this?]
```

## 3. Citation Appendix Formats (Mandatory)

### MLA 9
> Author. "Title of Source." *Title of Container*, Other contributors, Version, Number, Publisher, Publication date, Location.

### APA 7
> Author, A. A. (Year, Month Day). *Title of work*. Publisher. URL

### Legal (General)
> *Case Name*, Volume Source Page (Court Year).

## 4. Research Scope Brief (Varys)
To be generated at the start of Phase 1.

```markdown
# RESEARCH SCOPE BRIEF: [Project Name]
*   **Research Director:** Varys
*   **Date:** [YYYY-MM-DD]

## 1. Core Question(s)
*   [Primary Research Question]

## 2. Target Domains
*   [e.g., Legal, Medical, Historical]

## 3. Language Assumptions
*   [e.g., English (Primary), Vietnamese (Secondary)]

## 4. Source Quotas (Targets)
*   Tier 1: [5-15]
*   Tier 2: [8-20]
*   Tier 3: [8-20]
*   Tier 4: [≤5]

## 5. Coverage Checklist
*   [ ] Institutional Repositories
*   [ ] Academic Databases
*   [ ] Court Archives
*   [ ] [Specific Domain Archive]
```

## 5. Authority Packet (Domain Agents)
To be generated after primary retrieval by the assigned specialist (Portia, Samwell, etc.).

```markdown
# AUTHORITY PACKET
*   **Specialist:** [Agent Name]
*   **Domain:** [Legal/Medical/etc.]
*   **Focus:** Primary & Tier-1 Sources

## Tier 1 Candidates (Secured)
*   **[S-001]** [Title] - [Description]
*   **[S-002]** [Title] - [Description]

## Access Barriers
*   [Source Title]: [Reason for inaccessibility, e.g., Paywall, Physical Archive]
    *   *Workaround:* [Proposed solution]

## Laundering Checks
*   [ ] Replaced indirect citation X with original report Y.
```
