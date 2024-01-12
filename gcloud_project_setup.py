import subprocess
import uuid

def create_project(prefix):
    """Create a new Google Cloud project with a unique ID."""
    project_id = f"{prefix}-{uuid.uuid4().hex[:6]}"
    subprocess.run(["gcloud", "projects", "create", project_id, "--name", "Bay Crawler Project"], check=True)
    return project_id

def set_active_project(project_id):
    """Set the newly created project as the active project."""
    subprocess.run(["gcloud", "config", "set", "project", project_id], check=True)