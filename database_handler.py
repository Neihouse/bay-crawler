from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, DateTime
from sqlalchemy.orm import sessionmaker
from datetime import datetime

class DatabaseHandler:
    def __init__(self):
        self.engine = create_engine('mysql+pymysql://user:password@localhost/email_crawler')
        self.metadata = MetaData()
        self.emails = Table('emails', self.metadata,
                            Column('id', Integer, primary_key=True),
                            Column('email', String(255), nullable=False),
                            Column('source_url', String(255), nullable=False),
                            Column('timestamp', DateTime, default=datetime.utcnow))
        self.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def add_email(self, email, source_url):
        session = self.Session()
        session.add({'email': email, 'source_url': source_url})
        session.commit()
        session.close()