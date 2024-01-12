from google.cloud import compute_v1

class ComputeClient:
    def __init__(self):
        self.client = compute_v1.InstancesClient()

    def create_instance(self, instance_name):
        """Create a new compute instance."""
        # This is a simplified example. In practice, you would need to specify
        # more configuration details for the instance.
        project_id = 'your-gcp-project-id'
        zone = 'us-central1-a'
        machine_type = 'n1-standard-1'
        source_image = 'projects/debian-cloud/global/images/family/debian-10'
        instance = {
            'name': instance_name,
            'machine_type': machine_type,
            'disks': [{
                'boot': True,
                'initialize_params': {'source_image': source_image}
            }]
        }
        response = self.client.insert(project_id, zone, instance)
        print(f"Instance {instance_name} creation initiated: {response.operation.name}")