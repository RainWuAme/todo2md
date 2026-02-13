---
description: Sync completed Taskade tasks to Weekly Report (Home.md)
---

# Weekly Sync Workflow

Follow these steps to sync completed tasks from Taskade to the `Home.md` file using the `fetch_recent_tasks.py` script.

1.  **Fetch Tasks**:
    Run the python script to fetch all recently completed tasks from Taskade.
    ```bash
    python fetch_recent_tasks.py
    ```
    // turbo

2.  **Read Fetched Data**:
    Read the content of the generated `last_week_tasks.txt` file.
    ```bash
    cat last_week_tasks.txt
    ```
    // turbo

3.  **Summarize and Update**:
    - Based on the content of `last_week_tasks.txt`, generate a **Detailed and Comprehensive Report** in Markdown.
    - **Crucial**: Do NOT summarize too aggressively. The user wants to see the specific items they completed. Group related items, but ensure the **volume and specifics** of the work are visible.
    - **Language Rule**: The content must be in **English**. Keep technical terms in English.
    - **Format recommendation**:
        ```markdown
        ## YYMMDD ##
        
        ### Project Name
        #### Category/Sub-feature 1
        - Task details...
        - Task details...
        
        #### Category/Sub-feature 2
        - Task details...
        ```
    - Prepend this summary to `Home.md` using the `prepend_to_file` tool or `run_command` with echo/cat. 
    - Note: Ensure the `## YYMMDD ##` header matches today's date in that format (e.g., `240204`).
    
4.  **Cleanup**:
    Remove the temporary tasks file.
    ```bash
    rm last_week_tasks.txt
    ```
    // turbo

5.  **Notify User**:
    Inform the user that the sync is complete and `Home.md` has been updated.
