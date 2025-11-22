import sys
import os
from taskade_client import get_recently_completed_tasks, get_all_projects

def test_connection():
    print("Connecting to Taskade to fetch project list...")
    try:
        projects = get_all_projects()
        if not projects:
            print("No projects found.")
            return

        print("\nAvailable Projects:")
        print("0. [CHECK ALL PROJECTS]")
        for i, p in enumerate(projects):
            print(f"{i+1}. {p.get('name')}")

        choice = input("\nEnter the number of the project to check (default 0): ").strip()
        
        selected_project_name = None
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

        # Fetch tasks
        tasks_by_project = get_recently_completed_tasks(project_filter=selected_project_name)
        
        if not tasks_by_project:
            print("Connection successful, but no completed tasks found (or API returned empty list).")
            return

        print(f"\nSuccessfully fetched data from {len(tasks_by_project)} projects.")
        
        # Print a sample to verify content
        for p_name, tasks in tasks_by_project.items():
            print(f"\nProject: {p_name}")
            print(f"Found {len(tasks)} completed tasks.")
            if tasks:
                first_task = tasks[0]
                print(f"Sample task: {first_task.get('text', 'No text')}")
                print(f"Completed at: {first_task.get('completedAt', 'Unknown')}")

    except Exception as e:
        print(f"\n❌ Error connecting to Taskade: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Ensure we can find the module if running from same dir
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    test_connection()
