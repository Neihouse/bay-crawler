#!/bin/bash

# This script creates and configures the Cloud SQL instance for the "bay-crawler" project.

# Create a Cloud SQL instance
gcloud sql instances create bay-crawler-sql-instance \
    --tier=db-n1-standard-2 \
    --region=us-central1

# Set up the default database user and password
gcloud sql users set-password root --host=% --instance=bay-crawler-sql-instance --prompt-for-password

# Create a database for storing crawler data and LLM training datasets
gcloud sql databases create bay_crawler_db --instance=bay-crawler-sql-instance

echo "Cloud SQL instance setup complete."