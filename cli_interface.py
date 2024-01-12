import argparse

class CLIInterface:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description='Bay Area Event Production Company Email Crawler')
        self.parser.add_argument('--database', type=str, required=True, help='Database connection string')
        self.parser.add_argument('--sources', type=str, nargs='+', required=True, help='List of sources for seed URLs')
        self.args = self.parser.parse_args()

    def get_configuration(self):
        return {
            'database': self.args.database,
            'sources': self.args.sources
        }