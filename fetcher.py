import requests

class Fetcher:
    def fetch(self, url):
        response = requests.get(url)
        return response.text