import argparse

class CLI:
    def parse_arguments(self):
        parser = argparse.ArgumentParser(description='Bay Crawler CLI')
        parser.add_argument('--url', type=str, help='Starting URL for the crawler')
        parser.add_argument('--depth', type=int, help='Maximum depth to crawl')
        args = parser.parse_args()
        return args