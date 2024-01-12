import subprocess

class CloudSQLProxyManager:
    def __init__(self, project_id):
        self.project_id = project_id

    def setup_proxy(self, instance_name):
        """Download and configure the Cloud SQL Auth proxy."""
        subprocess.run([
            "wget", "https://dl.google.com/cloudsql/cloud_sql_proxy.linux.amd64",
            "-O", "cloud_sql_proxy"
        ], check=True)
        subprocess.run(["chmod", "+x", "cloud_sql_proxy"], check=True)
        subprocess.run([
            "./cloud_sql_proxy",
            "-instances={self.project_id}:{instance_name}=tcp:5432"
        ], check=True)