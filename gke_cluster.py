import subprocess

def create_gke_cluster():
    # Create a GKE cluster using the gcloud CLI
    subprocess.run([
        "gcloud", "container", "clusters", "create", "bay-crawler-cluster",
        "--zone", "us-central1-a"
    ], check=True)