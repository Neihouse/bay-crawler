import urllib.robotparser

class Robots:
    def __init__(self, url):
        self.parser = urllib.robotparser.RobotFileParser()
        self.parser.set_url(url)
        self.parser.read()

    def can_fetch(self, user_agent, url):
        return self.parser.can_fetch(user_agent, url)