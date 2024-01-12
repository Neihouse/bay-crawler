#!/bin/bash

# This script creates a service account and assigns necessary IAM roles.

# Create a service account for the Cloud SQL Auth proxy
SERVICE_ACCOUNT_NAME="cloud-sql-proxy-sa"
gcloud iam service-accounts create "$SERVICE_ACCOUNT_NAME" --display-name "Cloud SQL Proxy Service Account"

# Generate and download a key file for the service account
gcloud iam service-accounts keys create ~/key.json --iam-account "$SERVICE_ACCOUNT_NAME@$PROJECT_ID.iam.gserviceaccount.com"

# Assign the necessary IAM roles to the service account
gcloud projects add-iam-policy-binding "$PROJECT_ID" --member "serviceAccount:$SERVICE_ACCOUNT_NAME@$PROJECT_ID.iam.gserviceaccount.com" --role "roles/cloudsql.client"

echo "Service account setup is complete."