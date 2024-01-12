import requests

class URLFetcher:
    def fetch(self, url):
        response = requests.get(url)
        return response.text