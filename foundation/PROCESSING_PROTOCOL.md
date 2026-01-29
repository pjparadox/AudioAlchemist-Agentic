# Sub Team Six — Operational Protocols

## 1. The Recursive Modular Orchestrator
The system operates as an adversarial assembly line.

1.  **Mai (Generator):** Ingests Chunk. Outputs raw translation.
2.  **Quang (Adjudicator):** Queries `MASTER_KINSHIP_MAP`.
3.  **Linh (Context):** Checks `EPISODE_CONTEXT_BEATS`.
4.  **Vu (Gatekeeper):** Checks CPS limits.
    - *Pass:* Write to disk.
    - *Fail:* Trigger Recursion (Return to Mai).

## 2. The Context-Updating Loop
**Step A: READ**
Read the last entry in `PROGRESS_LOG.md`.

**Step B: PROCESS**
Translate Chunk N.

**Step C: UPDATE SUMMARY**
Append to `PROGRESS_LOG.md`:
- Chunk N status.
- **CUMULATIVE PLOT SUMMARY:** A 2-3 sentence update.

## 3. Output Persistence
- Save output immediately.
- Update `PROGRESS_LOG.md`.
- Clear memory.
