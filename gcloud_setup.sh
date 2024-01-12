#!/bin/bash

# This script sets up the Google Cloud environment for the "bay-crawler" project.

# Authenticate with Google Cloud
gcloud auth login

# Update gcloud components
gcloud components update

# Create a new Google Cloud project
PROJECT_ID="bay-crawler-$(date +%s)"
gcloud projects create "$PROJECT_ID" --name="Bay Crawler Project"
gcloud config set project "$PROJECT_ID"

# Enable necessary Google Cloud services
gcloud services enable compute.googleapis.com
gcloud services enable container.googleapis.com
gcloud services enable sqladmin.googleapis.com
gcloud services enable secretmanager.googleapis.com

# Create a Cloud SQL instance
CLOUD_SQL_INSTANCE_NAME="bay-crawler-sql-instance"
gcloud sql instances create "$CLOUD_SQL_INSTANCE_NAME" --tier=db-f1-micro --region=us-central1

# Set up the default database user and password
DB_USER="crawler_user"
DB_PASS="crawler_password"
gcloud sql users set-password "$DB_USER" --instance="$CLOUD_SQL_INSTANCE_NAME" --password="$DB_PASS"

# Create a database for storing crawler data
DATABASE_NAME="crawler_data"
gcloud sql databases create "$DATABASE_NAME" --instance="$CLOUD_SQL_INSTANCE_NAME"

echo "Google Cloud environment setup is complete."