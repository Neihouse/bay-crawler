#!/bin/bash

# This script sets up the Google Cloud environment for the "bay-crawler" project.

# Step 1: Set up the Google Cloud SDK and authenticate
gcloud components update
gcloud auth login

# Step 2: Project creation and configuration
PROJECT_ID="bay-crawler-$(date +%s)"
gcloud projects create "$PROJECT_ID" --name="Bay Crawler Project"
gcloud config set project "$PROJECT_ID"

# Step 3: Enable required services
gcloud services enable compute.googleapis.com
gcloud services enable container.googleapis.com
gcloud services enable sqladmin.googleapis.com
gcloud services enable secretmanager.googleapis.com

# Step 4: Cloud SQL instance creation and database setup
# Note: Replace with appropriate instance specifications
gcloud sql instances create bay-crawler-sql-instance --tier=db-f1-micro --region=us-central1
gcloud sql users set-password root --host=% --instance=bay-crawler-sql-instance --password=[YOUR_PASSWORD]
gcloud sql databases create bay_crawler_db --instance=bay-crawler-sql-instance

# Call other scripts to continue the setup
./create_service_account.sh
./configure_cloud_sql_proxy.sh