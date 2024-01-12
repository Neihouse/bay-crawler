class URLManager:
    def __init__(self, seed_urls):
        self.new_urls = set(seed_urls)
        self.old_urls = set()

    def has_new_url(self):
        return len(self.new_urls) > 0

    def get_new_url(self):
        url = self.new_urls.pop()
        self.old_urls.add(url)
        return url