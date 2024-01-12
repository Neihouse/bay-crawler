resource "google_secret_manager_secret" "crawler_secret" {
  secret_id = "crawler-secret"

  replication {
    automatic = true
  }
}

resource "google_secret_manager_secret_version" "crawler_secret_version" {
  secret      = google_secret_manager_secret.crawler_secret.id
  secret_data = "your-secret-data"
}