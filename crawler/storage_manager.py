from .models import EmailRecord
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

class StorageManager:
    def __init__(self, logger):
        self.logger = logger
        self.engine = create_engine('mysql+pymysql://user:password@localhost/dbname')
        self.Session = sessionmaker(bind=self.engine)

    def store_email(self, email, url):
        # Store the email record in the database
        session = self.Session()
        record = EmailRecord(email=email, source_url=url)
        session.add(record)
        session.commit()
        session.close()