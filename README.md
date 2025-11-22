# Todo2MD

Automate the extraction of completed tasks from [Taskade](https://www.taskade.com/) and summarize them into your local Markdown wiki (e.g., Obsidian, VSCode) or generate structured weekly reports.

## Features

-   **Fetch Completed Tasks**: Retrieves recently completed tasks from your Taskade projects.
-   **Project Filtering**: Select specific projects to process or check all of them.
-   **AI Summarization**: Uses a local LLM (via vLLM) to generate structured, human-readable summaries of your tasks.
-   **Markdown Integration**: Automatically appends the summaries to your `Home.md` file.
-   **Weekly Report Generation**: Parses `Home.md` and generates structured weekly reports with targeted updates to specific documentation files.

## Prerequisites

-   Python 3.12+
-   Conda environment: `llm_grn` (or similar with required packages)
-   Taskade API Key
-   Access to a vLLM endpoint (for summarization)

## Setup

1.  **Clone the repository** (if applicable).

2.  **Environment Setup**:
    Ensure you have the `llm_grn` conda environment or install dependencies manually:
    ```bash
    conda activate llm_grn
    pip install requests python-dotenv langchain-openai langgraph
    ```

3.  **Configuration**:
    Create a `.env` file in the root directory with the following variables:
    ```env
    TASKADE_API_KEY=your_taskade_api_key_here
    VLLM_BASE_URL=http://localhost:8000/v1
    VLLM_MODEL_NAME=hosted_vllm/model
    VLLM_API_KEY=EMPTY
    ```

## Usage

### 1. Test Connection
Run the interactive test script to verify your connection to Taskade and see your projects:

```bash
python test_taskade_connection.py
```
Follow the prompts to select a project or check all.

### 2. Update Daily Wiki
Run the main script to fetch new completed tasks, summarize them, and update your `Home.md`:

```bash
python update_wiki.py
```

### 3. Generate Weekly Report
Parse the latest week's content from `Home.md` and generate structured updates for your weekly report files:

```bash
python generate_weekly_report.py
```

This will:
- Extract the most recent week's tasks from `Home.md` (identified by date headers `## YYMMDD ##`)
- Use the LLM to categorize and summarize tasks
- Update specific report files in the `../ebi-weekly-report` directory
- Append a summary to the main research log with cross-references

## File Structure

### Core Files
-   `taskade_client.py`: Handles communication with the Taskade API.
-   `llm_client.py`: Manages the LLM connection for summarizing tasks and processing weekly reports.
-   `update_wiki.py`: Main orchestration script for daily task updates.
-   `generate_weekly_report.py`: Parses `Home.md` and generates structured weekly reports.

### Test Files
-   `test_taskade_connection.py`: Interactive utility to test Taskade API connectivity.
-   `test_integration.py`: Unit tests for the `update_wiki` module.
-   `test_langgraph_client.py`: Unit tests for the LLM client.

### Configuration & Output
-   `.env`: Configuration file for API keys (not committed).
-   `Home.md`: Daily task summary file (auto-generated).
-   `debug_output.txt`: Debug output from test runs (temporary).
