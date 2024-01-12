import subprocess

def create_sql_instance(project_id):
    """Create a Cloud SQL instance optimized for LLM training."""
    instance_name = "bay-crawler-sql-instance"
    subprocess.run([
        "gcloud", "sql", "instances", "create", instance_name,
        "--tier=db-n1-standard-2", "--region=us-central1",
        "--project", project_id
    ], check=True)

def setup_database(project_id):
    """Set up the default database and user for the Cloud SQL instance."""
    instance_name = "bay-crawler-sql-instance"
    database_name = "bay_crawler_db"
    subprocess.run([
        "gcloud", "sql", "databases", "create", database_name,
        "--instance", instance_name, "--project", project_id
    ], check=True)
    # Note: In a real-world scenario, you would also set up the database user and password here.