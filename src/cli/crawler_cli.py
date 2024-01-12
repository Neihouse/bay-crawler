import argparse

class CrawlerCLI:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description='Bay Crawler CLI')
        self.setup_arguments()

    def setup_arguments(self):
        # Set up CLI arguments
        pass

    def parse_arguments(self):
        # Parse CLI arguments
        return self.parser.parse_args()