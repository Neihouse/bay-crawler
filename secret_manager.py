import subprocess

def create_secret(secret_data):
    # Create a secret using the gcloud CLI
    subprocess.run([
        "echo", "-n", secret_data, "|", "gcloud", "secrets", "create",
        "bay-crawler-secret", "--data-file=-"
    ], check=True)