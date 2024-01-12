import subprocess

class GCloudAuthenticator:
    def authenticate(self):
        """Authenticate with Google Cloud using the gcloud CLI."""
        subprocess.run(["gcloud", "auth", "login"], check=True)