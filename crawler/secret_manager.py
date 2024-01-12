from google.cloud import secretmanager

class SecretManager:
    def __init__(self):
        self.client = secretmanager.SecretManagerServiceClient()

    def get_database_credentials(self):
        # Replace 'my-secret-name' and 'my-secret-version' with your secret's name and version
        name = f"projects/my-project/secrets/my-secret-name/versions/my-secret-version"
        response = self.client.access_secret_version(request={"name": name})
        return response.payload.data.decode("UTF-8")