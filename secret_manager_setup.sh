#!/bin/bash

# Manage secrets using Google Cloud Secret Manager

# Create a new secret with the name "bay-crawler-secret"
echo -n "secret-data" | gcloud secrets create bay-crawler-secret --data-file=-