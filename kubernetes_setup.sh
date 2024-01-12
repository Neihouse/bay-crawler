#!/bin/bash

# This script creates a Kubernetes cluster and configures kubectl.

# Create a Google Kubernetes Engine (GKE) cluster
CLUSTER_NAME="bay-crawler-cluster"
gcloud container clusters create "$CLUSTER_NAME" --zone us-central1-a

# Get credentials for the cluster
gcloud container clusters get-credentials "$CLUSTER_NAME" --zone us-central1-a

echo "Kubernetes cluster setup is complete."