import sys
from taskade_client import get_recently_completed_tasks

OUTPUT_FILE = "last_week_tasks.txt"

def main():
    print("Fetching completed tasks from Taskade...")
    try:
        # Fetches ALL completed tasks as per user instruction.
        tasks_by_project = get_recently_completed_tasks()
    except Exception as e:
        print(f"Error fetching tasks: {e}")
        return

    if not tasks_by_project:
        print("No completed tasks found.")
        # Create empty file to indicate no tasks
        with open(OUTPUT_FILE, "w") as f:
            f.write("No completed tasks found.")
        return

    print(f"Found tasks in {len(tasks_by_project)} projects.")
    
    with open(OUTPUT_FILE, "w") as f:
        f.write("# Recently Completed Tasks\n\n")
        f.write("Please summarize the following tasks for the weekly report:\n\n")
        
        for project_name, tasks in tasks_by_project.items():
            f.write(f"## Project: {project_name}\n")
            for task in tasks:
                # Basic sanitation of text
                text = task.get('text', 'No description').strip()
                completed_at = task.get('completedAt', 'N/A')
                f.write(f"- [x] {text} (Completed: {completed_at})\n")
            f.write("\n")

    print(f"Tasks saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
