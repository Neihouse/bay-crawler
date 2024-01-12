#!/bin/bash

# This script configures IAM roles and permissions for the "bay-crawler" project.

# Configure IAM roles and permissions as needed
# Example: Grant the Compute Viewer role to a user
gcloud projects add-iam-policy-binding "$PROJECT_ID" \
    --member user:example-user@gmail.com \
    --role roles/compute.viewer

echo "IAM setup complete."