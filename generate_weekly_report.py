import os
import re
import datetime
import subprocess
from typing import List, Dict
from llm_client import process_weekly_tasks

# Configuration
HOME_MD_PATH = "Home.md"
REPORT_DIR = "../ebi-weekly-report"
MAIN_LOG_FILE = "Research_Log_Refining_PKNs_with_LLMs.md"
AVAILABLE_FILES = [
    "Agent.md",
    "Ground_truth_data.md",
    "LLM_confidence.md",
    "With_vs_Without_Web_Search.md"
]

def parse_home_md(file_path: str) -> Dict[str, str]:
    """
    Parses Home.md to extract the latest week's content.
    Returns a dict with 'date' (YYYY-MM-DD) and 'content'.
    """
    with open(file_path, 'r') as f:
        content = f.read()

    # Find the first date header: ## DDMMYY ##
    match = re.search(r'^## (\d{6}) ##', content, re.MULTILINE)
    if not match:
        raise ValueError("No date header found in Home.md")

    date_str = match.group(1)
    # Convert YYMMDD to YYYY-MM-DD
    # Assuming 20xx
    year = "20" + date_str[0:2]
    month = date_str[2:4]
    day = date_str[4:6]
    formatted_date = f"{year}-{month}-{day}"

    # Extract content until the next header
    start_index = match.end()
    # Find the next ## header
    next_match = re.search(r'^## \d{6} ##', content[start_index:], re.MULTILINE)
    
    if next_match:
        week_content = content[start_index:start_index + next_match.start()].strip()
    else:
        week_content = content[start_index:].strip()

    return {
        "date": formatted_date,
        "content": week_content
    }

def prepend_to_file(filepath: str, content: str, date: str):
    """
    Prepends content to the top of a file using shell commands.
    Adds a date header if not present for that date.
    """
    # Check if file exists
    if not os.path.exists(filepath):
        # If file doesn't exist, create it with the content
        text_to_write = f"## {date}\n\n{content}\n"
        text_to_write_escaped = text_to_write.replace("'", "'\\''")
        cmd = f"echo '{text_to_write_escaped}' > {filepath}"
        subprocess.run(cmd, shell=True, check=True)
        print(f"Created {filepath}")
        return

    # Read existing content
    with open(filepath, 'r') as f:
        existing_content = f.read()

    # Check if date header exists
    header_exists = f"## {date}" in existing_content

    # Prepare content to prepend
    text_to_prepend = ""
    if not header_exists:
        text_to_prepend += f"## {date}\n\n"

    text_to_prepend += content + "\n\n"

    # Combine new content with existing content
    new_content = text_to_prepend + existing_content

    # Write back to file
    with open(filepath, 'w') as f:
        f.write(new_content)

    print(f"Prepended to {filepath}")

def main():
    print("Parsing Home.md...")
    try:
        data = parse_home_md(HOME_MD_PATH)
    except Exception as e:
        print(f"Error parsing Home.md: {e}")
        return

    date = data['date']
    content = data['content']
    print(f"Found content for date: {date}")

    print("Processing tasks with LLM...")
    result = process_weekly_tasks(content, AVAILABLE_FILES)
    
    if not result or not result.get('file_updates'):
        print("No updates generated.")
        return

    # Update specific files
    updated_files = []
    for update in result['file_updates']:
        target_file = update['target_file']
        if target_file not in AVAILABLE_FILES:
            print(f"Warning: Target file {target_file} not in available files. Skipping.")
            continue

        full_path = os.path.join(REPORT_DIR, target_file)
        prepend_to_file(full_path, update['content'], date)
        updated_files.append(target_file)

    # Update main log
    if result.get('main_summary'):
        main_log_path = os.path.join(REPORT_DIR, MAIN_LOG_FILE)

        # Construct the summary entry with links
        links = []
        for f in updated_files:
            # Remove extension for title if desired, or keep it
            title = f.replace('.md', '').replace('_', ' ')
            link = f"[{title}, {date}]({f}#{date})"
            links.append(link)

        links_str = " ".join(links)
        summary_entry = f"1. {result['main_summary']} {links_str}"

        prepend_to_file(main_log_path, summary_entry, date)

    print("Weekly report generation complete.")

if __name__ == "__main__":
    main()
