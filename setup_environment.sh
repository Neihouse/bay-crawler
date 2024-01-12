#!/bin/bash

# This script handles the initial setup and authentication, project creation,
# API enablement, and Cloud SQL instance creation for the "bay-crawler" project.

# Authenticate with Google Cloud
gcloud auth login

# Update gcloud components
gcloud components update

# Generate a unique project ID with a "bay-crawler" prefix and create the project
PROJECT_ID="bay-crawler-$(date +%s)"
gcloud projects create "$PROJECT_ID" --name="Bay Crawler Project"

# Set the newly created project as the active project
gcloud config set project "$PROJECT_ID"

# Enable necessary APIs for the project
gcloud services enable compute.googleapis.com
gcloud services enable container.googleapis.com
gcloud services enable sqladmin.googleapis.com
gcloud services enable secretmanager.googleapis.com

# Create a Cloud SQL instance optimized for LLM training
gcloud sql instances create bay-crawler-sql-instance \
    --database-version=POSTGRES_12 \
    --cpu=4 \
    --memory=15GB \
    --region=us-central1

# Set up the default database user and password
DB_USER="bay_crawler_user"
DB_PASS="your_strong_password_here" # Replace with a strong password
gcloud sql users set-password "$DB_USER" --instance=bay-crawler-sql-instance --password="$DB_PASS"

# Create a database for storing crawler data and LLM training datasets
gcloud sql databases create bay_crawler_db --instance=bay-crawler-sql-instance

echo "Environment setup is complete."