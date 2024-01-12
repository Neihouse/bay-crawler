import subprocess

class ServiceAccountManager:
    def __init__(self, project_id):
        self.project_id = project_id

    def create_service_account(self):
        """Create a service account for the Cloud SQL Auth proxy."""
        service_account_name = "bay-crawler-sql-proxy"
        subprocess.run([
            "gcloud", "iam", "service-accounts", "create", service_account_name,
            "--project", self.project_id
        ], check=True)
        return service_account_name

    def assign_roles(self):
        """Assign necessary IAM roles to the service account."""
        subprocess.run([
            "gcloud", "projects", "add-iam-policy-binding", self.project_id,
            "--member", "serviceAccount:bay-crawler-sql-proxy@{self.project_id}.iam.gserviceaccount.com",
            "--role", "roles/cloudsql.client"
        ], check=True)