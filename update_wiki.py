import os
import re
from taskade_client import get_recently_completed_tasks, get_all_projects
from llm_client import generate_summary

HOME_MD_PATH = "/nfs/research/saezrodriguez/rain/workspace/todo2md/Home.md"

def read_home_md():
    if not os.path.exists(HOME_MD_PATH):
        return ""
    with open(HOME_MD_PATH, 'r') as f:
        return f.read()

def extract_existing_tasks(content):
    """
    Extracts all task texts from the content to use for de-duplication.
    Normalizes text by removing markdown list markers and whitespace.
    """
    tasks = set()
    for line in content.splitlines():
        line = line.strip()
        match = re.match(r'^([-*+]|\d+\.)\s+(.*)', line)
        if match:
            task_text = match.group(2).strip()
            tasks.add(task_text)
    return tasks

def format_tasks_for_llm(tasks):
    """
    Formats tasks into a simple text list for the LLM prompt.
    """
    lines = []
    for t in tasks:
        text = t.get('text', '').strip()
        # We could include hierarchy hints if available, but flat list might be enough for LLM to figure out context
        # if the text is descriptive.
        # Let's try to include parent info if we can, but for now just the text.
        lines.append(f"- {text}")
    return "\n".join(lines)

import datetime

def update_home_md():
    # Interactive Project Selection
    print("Connecting to Taskade to fetch project list...")
    projects = get_all_projects()
    selected_project_name = None
    
    if projects:
        print("\nAvailable Projects:")
        print("0. [CHECK ALL PROJECTS]")
        for i, p in enumerate(projects):
            print(f"{i+1}. {p.get('name')}")

        choice = input("\nEnter the number of the project to check (default 0): ").strip()
        
        if choice and choice != '0':
            try:
                idx = int(choice) - 1
                if 0 <= idx < len(projects):
                    selected_project_name = projects[idx].get('name')
                    print(f"\nSelected project: {selected_project_name}")
                else:
                    print("Invalid selection, checking all projects.")
            except ValueError:
                print("Invalid input, checking all projects.")
        else:
            print("\nChecking ALL projects...")
    else:
        print("No projects found or failed to fetch projects.")

    content = read_home_md()
    
    # Fetch tasks
    tasks_by_project = get_recently_completed_tasks(project_filter=selected_project_name)
    
    new_content_blocks = []
    
    for project_name, tasks in tasks_by_project.items():
        if not tasks:
            continue
            
        print(f"Project {project_name}: {len(tasks)} tasks found.")
        
        # Format for LLM
        tasks_text = format_tasks_for_llm(tasks)
        
        # Generate summary
        print(f"Generating summary for {project_name}...")
        summary = generate_summary(tasks_text)
        
        if summary:
            new_content_blocks.append(f"### {project_name}\n\n{summary}")

    if not new_content_blocks:
        print("No tasks found to summarize.")
        return

    # Prepare new content with date header
    today_str = datetime.datetime.now().strftime("%y%m%d")
    header = f"## {today_str} ##"
    
    new_section = "\n\n".join(new_content_blocks)
    
    # Check if today's header is already at the top
    lines = content.splitlines()
    if lines and lines[0].strip() == header:
        # Append to existing section (insert after header)
        # Actually, user said "add the text in the top". 
        # If header exists, maybe we should just add it right after the header?
        # Or maybe just prepend the new blocks after the header.
        final_content = f"{header}\n\n{new_section}\n\n" + "\n".join(lines[1:])
    else:
        # Prepend new header and content
        final_content = f"{header}\n\n{new_section}\n\n{content}"
    
    with open(HOME_MD_PATH, 'w') as f:
        f.write(final_content)
        
    print(f"Updated Home.md with {len(new_content_blocks)} blocks of summaries.")

if __name__ == "__main__":
    update_home_md()
