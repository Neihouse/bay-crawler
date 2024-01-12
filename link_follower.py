from bs4 import BeautifulSoup

class LinkFollower:
    @staticmethod
    def get_links(html_content):
        soup = BeautifulSoup(html_content, 'html.parser')
        return [link.get('href') for link in soup.find_all('a')]