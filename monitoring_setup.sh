#!/bin/bash

# This script sets up monitoring and logging for the application.

# Enable Google Cloud Operations Suite services
gcloud services enable monitoring.googleapis.com
gcloud services enable logging.googleapis.com

echo "Monitoring and logging setup is complete."