from google.cloud import compute_v1

class ComputeManager:
    def __init__(self):
        self.client = compute_v1.InstancesClient()

    def create_instance(self, project_id, zone, instance_name):
        """Create a compute instance in GCP."""
        instance = compute_v1.Instance(name=instance_name)
        # Additional instance configuration goes here
        response = self.client.insert(project=project_id, zone=zone, instance_resource=instance)
        print(f"Instance {instance_name} created.")