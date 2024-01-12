#!/bin/bash

# Create a Google Kubernetes Engine (GKE) cluster

# Note: Replace CLUSTER_NAME and ZONE with appropriate values
CLUSTER_NAME="bay-crawler-cluster"
ZONE="us-central1-a"

# Create the GKE cluster
gcloud container clusters create "$CLUSTER_NAME" --zone "$ZONE"