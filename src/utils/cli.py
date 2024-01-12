import argparse

class CLI:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description='Bay Crawler CLI')
        # Define CLI arguments here

    def parse_arguments(self):
        return self.parser.parse_args()