import os
import requests
from typing import List, Dict, Any

class TaskadeClient:
    def __init__(self, api_key: str, base_url: str = "https://www.taskade.com/api/v1"):
        if not api_key:
            raise ValueError("Taskade API key is required.")
        self.api_key = api_key
        self.base_url = base_url
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def _make_request(self, method: str, endpoint: str, params: Dict = None, data: Dict = None) -> Dict[str, Any]:
        url = f"{self.base_url}/{endpoint}"
        try:
            response = requests.request(method, url, headers=self.headers, params=params, json=data)
            response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            print(f"Response content: {response.text}")
            raise
        except requests.exceptions.ConnectionError as conn_err:
            print(f"Error Connecting: {conn_err}")
            raise
        except requests.exceptions.Timeout as timeout_err:
            print(f"Timeout Error: {timeout_err}")
            raise
        except requests.exceptions.RequestException as req_err:
            print(f"An unexpected error occurred: {req_err}")
            raise

    def fetch_projects(self) -> List[Dict[str, Any]]:
        """
        Fetches all projects accessible by the API key.
        """
        print("Fetching projects...")
        return self._make_request("GET", "projects")

    def fetch_tasks_in_project(self, project_id: str) -> List[Dict[str, Any]]:
        """
        Fetches all tasks within a specific project.
        The Taskade API documentation is not publicly detailed,
        so this endpoint is an educated guess based on common REST API patterns.
        """
        print(f"Fetching tasks for project ID: {project_id}...")
        # This endpoint might need adjustment based on actual Taskade API structure
        # Common patterns: projects/{id}/tasks, projects/{id}/nodes, etc.
        # Without explicit documentation, this is a best guess.
        return self._make_request("GET", f"projects/{project_id}/tasks")

    def fetch_completed_tasks(self, project_id: str) -> List[Dict[str, Any]]:
        """
        Fetches completed tasks for a given project.
        This method will likely require filtering the results from fetch_tasks_in_project
        or a specific endpoint if available in the Taskade API.
        """
        print(f"Fetching completed tasks for project ID: {project_id}...")
        # Placeholder: Actual filtering logic will depend on the structure of task objects
        # returned by the Taskade API.
        all_tasks = self.fetch_tasks_in_project(project_id)
        completed_tasks = [task for task in all_tasks if task.get('status') == 'completed'] # Assuming a 'status' field
        return completed_tasks

if __name__ == "__main__":
    # Example usage (requires .env to be set up)
    from dotenv import load_dotenv
    load_dotenv()

    TASKADE_API_KEY = os.getenv("TASKADE_API_KEY")
    TASKADE_PROJECT_ID = os.getenv("TASKADE_PROJECT_ID")

    if not TASKADE_API_KEY:
        print("Error: TASKADE_API_KEY not found in environment variables.")
    elif not TASKADE_PROJECT_ID:
        print("Error: TASKADE_PROJECT_ID not found in environment variables.")
    else:
        try:
            client = TaskadeClient(api_key=TASKADE_API_KEY)
            
            # Example: Fetch all projects
            projects = client.fetch_projects()
            print(f"Found {len(projects)} projects.")
            # for p in projects:
            #     print(f"- {p.get('name')} (ID: {p.get('id')})")

            # Example: Fetch tasks from a specific project
            # tasks = client.fetch_tasks_in_project(TASKADE_PROJECT_ID)
            # print(f"Found {len(tasks)} tasks in project {TASKADE_PROJECT_ID}.")

            # Example: Fetch completed tasks from a specific project
            completed_tasks = client.fetch_completed_tasks(TASKADE_PROJECT_ID)
            print(f"Found {len(completed_tasks)} completed tasks in project {TASKADE_PROJECT_ID}.")
            for task in completed_tasks:
                print(f"- {task.get('name')} (Status: {task.get('status')})")

        except ValueError as e:
            print(f"Configuration Error: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")
