import subprocess

def create_kubernetes_cluster(project_id):
    """Create a Kubernetes cluster for the crawler application."""
    cluster_name = "bay-crawler-cluster"
    subprocess.run([
        "gcloud", "container", "clusters", "create", cluster_name,
        "--zone", "us-central1-a", "--project", project_id
    ], check=True)