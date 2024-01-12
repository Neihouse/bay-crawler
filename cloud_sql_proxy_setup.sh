#!/bin/bash

# This script sets up the Cloud SQL Auth proxy.

# Download the Cloud SQL Auth proxy
wget https://dl.google.com/cloudsql/cloud_sql_proxy.linux.amd64 -O cloud_sql_proxy
chmod +x cloud_sql_proxy

# Start the proxy to enable a secure connection to the Cloud SQL instance
./cloud_sql_proxy -instances="$PROJECT_ID:$CLOUD_SQL_INSTANCE_NAME"=tcp:3306 &

echo "Cloud SQL Auth proxy setup is complete."