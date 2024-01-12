from email_extractor import EmailExtractor
import pytest

@pytest.fixture
def extractor():
    return EmailExtractor()

def test_extract_emails(extractor):
    sample_text = "Contact us at info@example.com or support@example.org."
    emails = extractor.extract_emails(sample_text)
    assert "info@example.com" in emails
    assert "support@example.org" in emails