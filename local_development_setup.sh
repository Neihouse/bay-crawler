#!/bin/bash

# This script configures the local development environment to connect to the Cloud SQL instance.

# Set environment variables for the local development
export DB_USER="bay_crawler_user"
export DB_PASS="your_strong_password_here" # Replace with the actual password
export DB_NAME="bay_crawler_db"
export DB_INSTANCE_CONNECTION_NAME="<YOUR_INSTANCE_CONNECTION_NAME>" # Replace with the actual instance connection name

# Configure local development tools and IDEs as needed

echo "Local development environment is configured."