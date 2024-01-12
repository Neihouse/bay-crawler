import subprocess

def authenticate_gcloud():
    """Authenticate with Google Cloud using the gcloud CLI."""
    subprocess.run(["gcloud", "auth", "login"], check=True)