import argparse

class CLI:
    def parse_arguments(self):
        parser = argparse.ArgumentParser(description="Bay Crawler CLI")
        parser.add_argument('--url', required=True, help='The starting URL for the crawler')
        parser.add_argument('--depth', type=int, default=1, help='The depth of the crawl')
        return parser.parse_args()