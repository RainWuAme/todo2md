import argparse
import os
import re
import datetime
from taskade_client import get_recently_completed_tasks, get_all_projects

# --- Configuration ---
# The path to your Home.md file. It's assumed to be in the same directory as this script.
HOME_MD_PATH = os.path.join(os.path.dirname(__file__), "Home.md")

# --- Helper Functions ---
def read_home_md():
    """Reads the content of the Home.md file."""
    if not os.path.exists(HOME_MD_PATH):
        print(f"Warning: {HOME_MD_PATH} not found. Creating a new one if content is generated.")
        return ""
    with open(HOME_MD_PATH, 'r', encoding='utf-8') as f:
        return f.read()

def write_home_md(content):
    """Writes the content to the Home.md file."""
    with open(HOME_MD_PATH, 'w', encoding='utf-8') as f:
        f.write(content)

def format_tasks_for_summarization(tasks):
    """
    Formats tasks into a simple text list suitable for summarization by an LLM.
    """
    lines = []
    for t in tasks:
        text = t.get('text', '').strip()
        if text: # Ensure there's actual text
            lines.append(f"- {text}")
    return "\n".join(lines)

# --- Main Logic ---
def generate_and_update_report_step1(project_choice=None):
    """
    Generates summaries of recently completed tasks from Taskade and updates Home.md.
    This version prepares the task text for summarization by the agent.
    """
    # 1. Interactive Project Selection
    print("Connecting to Taskade to fetch project list...")
    try:
        projects = get_all_projects()
    except Exception as e:
        print(f"Error fetching projects from Taskade: {e}")
        print("Please ensure TASKADE_API_KEY is set in your environment variables or .env file.")
        return None, None # Return None to indicate failure

    selected_project_name = None
    
    if projects:
        print("\nAvailable Projects:")
        print("0. [CHECK ALL PROJECTS]")
        for i, p in enumerate(projects):
            print(f"{i+1}. {p.get('name')}")

        if project_choice is not None:
            choice = str(project_choice)
            print(f"\nUsing provided project choice: {choice}")
        else:
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
        print("Please ensure your Taskade API key is valid and you have projects.")
        return None, None

    # 2. Fetch completed tasks
    print("Fetching recently completed tasks...")
    try:
        tasks_by_project = get_recently_completed_tasks(project_filter=selected_project_name)
    except Exception as e:
        print(f"Error fetching completed tasks: {e}")
        print("Ensure Taskade API key is valid and there are completed tasks.")
        return None, None

    # Store tasks to be summarized
    tasks_for_agent_summarization = []
    
    if not tasks_by_project:
        print("No completed tasks found for the selected project(s).")
        return None, None

    for project_name, tasks in tasks_by_project.items():
        if not tasks:
            continue
            
        print(f"Project '{project_name}': {len(tasks)} completed tasks found.")
        
        tasks_text = format_tasks_for_summarization(tasks)
        
        if tasks_text:
            tasks_for_agent_summarization.append({"project_name": project_name, "tasks_text": tasks_text})
        else:
            print(f"No tasks text to summarize for project '{project_name}'.")

    if not tasks_for_agent_summarization:
        print("No tasks found that require summarization.")
        return None, None
    
    # 3. Prepare new content blocks with placeholders for agent summarization
    content = read_home_md()
    today_str = datetime.datetime.now().strftime("%Y-%m-%d")
    header = f"## {today_str} Weekly Update ##"
    
    new_section_placeholders = []
    for item in tasks_for_agent_summarization:
        # Using a more unique and identifiable placeholder format
        placeholder = f"<!-- AGENT_SUMMARY_PLACEHOLDER_FOR_PROJECT_{item['project_name'].replace(' ', '_').replace('.', '').upper()} -->"
        new_section_placeholders.append(f"### {item['project_name']}\n\n{placeholder}")
    
    new_section = "\n\n".join(new_section_placeholders)

    lines = content.splitlines()
    final_content_with_placeholders = ""

    if lines and lines[0].strip() == header:
        remaining_content = "\n".join(lines[1:])
        final_content_with_placeholders = f"{header}\n\n{new_section}\n\n{remaining_content}"
    else:
        final_content_with_placeholders = f"{header}\n\n{new_section}\n\n{content}"
    
    # These print statements are critical for me (the agent) to intercept the data.
    print("\n--- AGENT_ACTION_REQUIRED_START ---")
    print("The following tasks need to be summarized by the Gemini CLI agent:")
    for item in tasks_for_agent_summarization:
        print(f"\n--- PROJECT: {item['project_name']} ---")
        print(item['tasks_text'])
        print(f"--- END_PROJECT: {item['project_name']} ---")
    print("\n--- AGENT_ACTION_REQUIRED_END ---")
    
    print("\n--- HOME_MD_CONTENT_WITH_PLACEHOLDERS_START ---")
    print(final_content_with_placeholders)
    print("--- HOME_MD_CONTENT_WITH_PLACEHOLDERS_END ---")
    
    return tasks_for_agent_summarization, final_content_with_placeholders


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate weekly report from Taskade tasks.")
    parser.add_argument("--project-choice", type=int, help="Specify the project choice (0 for all projects, 1+ for specific project).")
    args = parser.parse_args()
    
    generate_and_update_report_step1(project_choice=args.project_choice)
