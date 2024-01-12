import subprocess

def create_secret(project_id, secret_name, secret_data):
    """Create a secret in Google Cloud Secret Manager."""
    subprocess.run([
        "echo", "-n", secret_data, "|",
        "gcloud", "secrets", "create", secret_name, "--data-file=-",
        "--project", project_id
    ], check=True)