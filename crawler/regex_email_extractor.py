```python
import re

class RegexEmailExtractor:
    def __init__(self):
        self.email_regex = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')

    def extract_emails(self, text):
        return self.email_regex.findall(text)
```