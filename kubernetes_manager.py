from google.cloud import container_v1

class KubernetesManager:
    def __init__(self):
        self.client = container_v1.ClusterManagerClient()

    def create_cluster(self, project_id, zone, cluster_name):
        """Create a Kubernetes cluster in GCP."""
        cluster = container_v1.Cluster(name=cluster_name)
        # Additional cluster configuration goes here
        response = self.client.create_cluster(project_id, zone, cluster)
        print(f"Cluster {cluster_name} created.")