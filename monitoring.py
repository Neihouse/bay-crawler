import logging

def setup_logging():
    """Set up logging for the application."""
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger('bay-crawler')
    logger.info("Logging is set up.")

def monitor_resources():
    """Monitor GCP resource usage."""
    # This function would use GCP's monitoring APIs to track resource usage.
    # For simplicity, we are just printing a message here.
    print("Monitoring GCP resources.")