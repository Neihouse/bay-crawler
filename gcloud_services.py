import subprocess

def enable_services(project_id):
    """Enable required Google Cloud services for the project."""
    services = [
        "compute.googleapis.com",
        "container.googleapis.com",
        "sqladmin.googleapis.com",
        "secretmanager.googleapis.com"
    ]
    for service in services:
        subprocess.run(["gcloud", "services", "enable", service, "--project", project_id], check=True)