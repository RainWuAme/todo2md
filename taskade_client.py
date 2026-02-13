import requests
import datetime
import os

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("TASKADE_API_KEY")
if not API_KEY:
    raise ValueError("TASKADE_API_KEY environment variable not set")
BASE_URL = "https://www.taskade.com/api/v1"

import time

def get_headers():
    return {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

def make_request(url):
    max_retries = 5
    for i in range(max_retries):
        try:
            response = requests.get(url, headers=get_headers())
            if response.status_code == 429:
                wait_time = 5 * (i + 1)
                print(f"Rate limit hit. Waiting {wait_time} seconds...")
                time.sleep(wait_time)
                continue
            response.raise_for_status()
            return response
        except Exception as e:
            print(f"Request failed: {e}")
            if i == max_retries - 1:
                return None
            time.sleep(2)
    return None

def get_all_projects():
    """
    Returns a list of all projects from /me/projects
    """
    url = f"{BASE_URL}/me/projects"
    try:
        response = make_request(url)
        if not response:
            return []
        data = response.json()
        return data.get('items', []) if isinstance(data, dict) else data
    except Exception as e:
        print(f"Error fetching projects: {e}")
        return []

def get_tasks_from_project(project_id):
    """
    Fetches all tasks from a project.
    """
    url = f"{BASE_URL}/projects/{project_id}/tasks"
    try:
        response = make_request(url)
        if not response:
            return []
        return response.json().get('items', [])
    except Exception as e:
        print(f"Error fetching tasks for project {project_id}: {e}")
        return []

def get_recently_completed_tasks(project_filter=None):
    """
    Fetches ALL completed tasks from projects.
    User handles the time-window logic themselves (e.g. by clearing old tasks).
    Returns a dict: {project_name: [tasks]}
    """
    projects = get_all_projects()
    results = {}
    
    for project in projects:
        p_id = project.get('id')
        p_name = project.get('name')
        
        if project_filter and p_name != project_filter:
            continue
            
        print(f"Checking project: {p_name}...")
        
        tasks = get_tasks_from_project(p_id)
        completed_tasks = []
        
        for task in tasks:
            # Check if completed
            if task.get('completed'):
                completed_tasks.append(task)
       
        if completed_tasks:
            results[p_name] = completed_tasks
            
    return results

if __name__ == "__main__":
    # Test fetching
    tasks_by_project = get_recently_completed_tasks()
    
    # Debug: print one task to see fields
    if tasks_by_project:
        first_project = list(tasks_by_project.values())[0]
        if first_project:
            print(f"DEBUG: First task object: {first_project[0]}")

    for p_name, tasks in tasks_by_project.items():
        print(f"\nProject: {p_name}")
        for t in tasks:
            print(f"- [x] {t.get('text')} (Completed at: {t.get('completedAt')})")

