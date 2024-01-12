import subprocess

def create_service_account(project_id):
    """Create a service account for the Cloud SQL Auth proxy."""
    service_account_name = "bay-crawler-sql-proxy"
    subprocess.run([
        "gcloud", "iam", "service-accounts", "create", service_account_name,
        "--project", project_id
    ], check=True)
    return {
        "name": service_account_name,
        "project_id": project_id
    }

def generate_service_account_key(service_account_info):
    """Generate and download a key file for the service account."""
    service_account_email = f"{service_account_info['name']}@{service_account_info['project_id']}.iam.gserviceaccount.com"
    subprocess.run([
        "gcloud", "iam", "service-accounts", "keys", "create",
        "--iam-account", service_account_email, "service-account-key.json"
    ], check=True)