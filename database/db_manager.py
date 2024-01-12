from .models import Session, EventCompany

class DatabaseManager:
    def __init__(self):
        self.session = Session()

    def add_company(self, item):
        company = EventCompany(
            company_name=item['company_name'],
            email=item['email'],
            source_url=item['source_url']
        )
        self.session.add(company)
        self.session.commit()