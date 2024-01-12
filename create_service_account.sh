#!/bin/bash

# This script creates a service account and generates a key file for it.

# Set variables for the service account
SERVICE_ACCOUNT_NAME="bay-crawler-sql-proxy-sa"
PROJECT_ID=$(gcloud config get-value project)

# Create the service account
gcloud iam service-accounts create "$SERVICE_ACCOUNT_NAME" \
    --description="Service account for Cloud SQL Auth proxy" \
    --display-name="Bay Crawler SQL Proxy SA"

# Generate and download a key file for the service account
gcloud iam service-accounts keys create ~/bay-crawler-sql-proxy-key.json \
    --iam-account="$SERVICE_ACCOUNT_NAME@$PROJECT_ID.iam.gserviceaccount.com"

# Assign the necessary IAM roles to the service account
gcloud projects add-iam-policy-binding "$PROJECT_ID" \
    --member="serviceAccount:$SERVICE_ACCOUNT_NAME@$PROJECT_ID.iam.gserviceaccount.com" \
    --role="roles/cloudsql.client"

echo "Service account and key generation is complete."