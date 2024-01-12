from crawler.utils import extract_emails

def test_extract_emails():
    text = "Contact us at info@example.com or support@example.org"
    emails = extract_emails(text)
    assert len(emails) == 2
    assert "info@example.com" in emails
    assert "support@example.org" in emails

def test_compliance_checker_class():
    # Add tests for the ComplianceChecker class here
    pass