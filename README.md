# Todo2MD (Agentic Version)

Automate the extraction of completed tasks from [Taskade](https://www.taskade.com/) and summarize them into your `Home.md` using an Agentic Workflow (Antigravity).

## Workflow

Instead of running automated scripts that try to do everything (and often fail at the LLM step), this project now follows an **Agentic Workflow**.

1.  **Fetch Data**: You run a simple script to fetch raw data.
2.  **Agent Execution**: You ask the AI Agent (Antigravity) to process that data and update your report.

## Prerequisites

-   Python 3.12+
-   `TASKADE_API_KEY` set in your `.env` file.
-   Dependencies: `requests`, `python-dotenv`

## Setup

1.  **Install Dependencies**:
    ```bash
    pip install requests python-dotenv
    ```

2.  **Configuration**:
    Create a `.env` file in the root directory:
    ```env
    TASKADE_API_KEY=your_taskade_api_key_here
    ```

## Usage

### Weekly Sync

**Just ask the Agent:**

> "Execute tasks/weekly_sync.md"
> *OR*
> "Run the weekly sync"

**The Agent will automatically:**
1.  Run `python fetch_recent_tasks.py` to fetch data.
2.  Read the fetched tasks.
3.  Summarize them into `Home.md`.
4.  Clean up temporary files.

You do **not** need to run the python script yourself.

## Files

-   `fetch_recent_tasks.py`: Fetches completed tasks from Taskade.
-   `tasks/weekly_sync.md`: The "brain" or workflow guide for the Agent.
-   `taskade_client.py`: API client logic.
-   `Home.md`: Your weekly report destination.
