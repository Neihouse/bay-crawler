import subprocess
import uuid

class ProjectManager:
    def create_project(self, prefix):
        """Create a new Google Cloud project with a unique ID."""
        project_id = f"{prefix}-{uuid.uuid4().hex[:6]}"
        subprocess.run(["gcloud", "projects", "create", project_id], check=True)
        return project_id

    def set_active_project(self, project_id):
        """Set the active Google Cloud project."""
        subprocess.run(["gcloud", "config", "set", "project", project_id], check=True)