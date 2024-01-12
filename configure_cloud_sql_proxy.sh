#!/bin/bash

# This script downloads, configures, and starts the Cloud SQL Auth proxy.

# Download the Cloud SQL Auth proxy
wget https://dl.google.com/cloudsql/cloud_sql_proxy.linux.amd64 -O cloud_sql_proxy
chmod +x cloud_sql_proxy

# Start the proxy to enable a secure connection to the Cloud SQL instance
./cloud_sql_proxy -instances=<YOUR_INSTANCE_CONNECTION_NAME>=tcp:5432 \
    -credential_file=~/bay-crawler-sql-proxy-key.json &

echo "Cloud SQL Auth proxy is configured and running."