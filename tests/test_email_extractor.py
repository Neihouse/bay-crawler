from email_extractor import EmailExtractor
import pytest

@pytest.fixture
def email_extractor():
    return EmailExtractor()

def test_extract_emails(email_extractor):
    sample_text = "Contact us at info@example.com"
    emails = email_extractor.extract_emails(sample_text)
    assert "info@example.com" in emails