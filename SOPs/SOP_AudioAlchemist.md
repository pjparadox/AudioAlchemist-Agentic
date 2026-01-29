# Standard Operating Procedure: Audio Alchemy

**Objective:** Transform raw audio recordings (stems, jams, home recordings) into precision-sliced, labeled, and described instrument samples for Ableton Live 11.

**Team:** Audio Alchemist
*   **Apollo:** Director & QC.
*   **Pan:** Technical Slicer (Script Operator).
*   **Euterpe:** Sonic Describer (Metadata).

## Phase 1: Ingestion (Apollo)
1.  **Source Check:** Verify files in `input_alchemist/`. Supported formats: MP3, WAV.
2.  **Context Check:** Identify the source nature (e.g., "EDM Stem", "Violin Solo", "Folk Guitar").
3.  **Command:** Instruct **Pan** to process the files.

## Phase 2: Slicing & Analysis (Pan)
1.  **Execution:** Run the slicing tool.
    ```bash
    python3 tools_audio_slicer.py --input input_alchemist --output output_alchemist/temp
    ```
2.  **Verification:** Check the terminal output for errors.
3.  **Handoff:** Locate `output_alchemist/temp/slicing_report.json` and present it to the team.

## Phase 3: Description & Naming (Euterpe)
1.  **Ingest Data:** Read the JSON report.
2.  **Analyze Features:** For each slice, interpret the `features` (Centroid, Rolloff, ZCR) relative to the `velocity` and `source_file`.
3.  **Generate Description:** Create a short, evocative tag (max 15 chars).
    *   *Example:* High Brightness -> "Glassy"
    *   *Example:* Low Brightness + High Velocity -> "Punchy"
4.  **Rename Proposal:** Submit a rename list to Apollo.
    *   Target format: `[Source]_[Note]_[Velocity]_[Description].wav`

## Phase 4: Finalization (Apollo)
1.  **Review:** Audit the proposed names for consistency and Ableton compatibility.
    *   *Rule:* No spaces in filenames.
    *   *Rule:* Velocity must be 0-127.
    *   *Rule:* Notes must be standard (C4, F#3, etc.).
2.  **Commit:** (Simulated) Rename the files in `output_alchemist/temp/` and move them to `output_alchemist/final/`.
3.  **Clean Up:** Delete the temporary JSON report and original temp files if necessary.

## Exception Handling
*   **No Onsets Detected:** Pan reports "Silence or Continuous Drone". Apollo advises manual checking or different script parameters (if available).
*   **Unknown Pitch:** Pan marks note as "Unknown". Apollo decides whether to keep it as "Percussion" or discard.
