import subprocess

class ServiceManager:
    def __init__(self, project_id):
        self.project_id = project_id

    def enable_services(self):
        """Enable required Google Cloud services for the project."""
        services = [
            "compute.googleapis.com",
            "container.googleapis.com",
            "sqladmin.googleapis.com",
            "secretmanager.googleapis.com"
        ]
        for service in services:
            subprocess.run(["gcloud", "services", "enable", service, "--project", self.project_id], check=True)