import argparse

class CLIInterface:
    def parse_arguments(self):
        parser = argparse.ArgumentParser(description="Bay Crawler CLI")
        parser.add_argument('--config', help='Path to configuration file', required=True)
        return parser.parse_args()