#!/bin/bash

# This script manages secrets using Google Cloud Secret Manager for the "bay-crawler" project.

# Create a new secret with the name "bay-crawler-secret"
echo -n "secret-data" | gcloud secrets create bay-crawler-secret --data-file=-

echo "Secrets setup complete."