import subprocess

class CloudSQLManager:
    def __init__(self, project_id):
        self.project_id = project_id

    def create_instance(self):
        """Create a Cloud SQL instance optimized for LLM training."""
        instance_name = "bay-crawler-sql-instance"
        subprocess.run([
            "gcloud", "sql", "instances", "create", instance_name,
            "--tier=db-custom-8-30720",
            "--region=us-central1",
            "--project", self.project_id
        ], check=True)
        return instance_name

    def setup_database(self, instance_name):
        """Set up the default database and user for the Cloud SQL instance."""
        subprocess.run([
            "gcloud", "sql", "databases", "create", "crawler_db",
            "--instance", instance_name,
            "--project", self.project_id
        ], check=True)
        subprocess.run([
            "gcloud", "sql", "users", "set-password", "root",
            "--host=%",
            "--instance", instance_name,
            "--password", "root-password",
            "--project", self.project_id
        ], check=True)