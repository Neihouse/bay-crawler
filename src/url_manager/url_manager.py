class URLManager:
    def __init__(self):
        self.urls_to_visit = set()
        self.visited_urls = set()

    def add_url(self, url):
        if url not in self.visited_urls:
            self.urls_to_visit.add(url)

    def get_next_url(self):
        return self.urls_to_visit.pop()

    def mark_visited(self, url):
        self.visited_urls.add(url)
        self.urls_to_visit.discard(url)