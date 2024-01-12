provider "google" {
  credentials = file("<PATH_TO_YOUR_SERVICE_ACCOUNT_KEY>")
  project     = "<YOUR_PROJECT_ID>"
  region      = "us-central1"
}

resource "google_container_cluster" "crawler_cluster" {
  name     = "crawler-cluster"
  location = "us-central1"

  # Define the node pool configuration
  node_pool {
    name       = "default-pool"
    node_count = 3

    node_config {
      machine_type = "e2-medium"
      disk_size_gb = 100
    }
  }
}