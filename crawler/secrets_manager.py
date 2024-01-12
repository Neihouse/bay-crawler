from google.cloud import secretmanager

def get_secret(secret_id):
    # Create the Secret Manager client.
    client = secretmanager.SecretManagerServiceClient()
    # Build the resource name of the secret version.
    name = f"projects/my-project/secrets/{secret_id}/versions/latest"
    # Access the secret version.
    response = client.access_secret_version(request={"name": name})
    # Return the decoded payload.
    return response.payload.data.decode('UTF-8')