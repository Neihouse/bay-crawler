from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, DateTime
from datetime import datetime

class DatabaseManager:
    def __init__(self):
        self.engine = create_engine('mysql+pymysql://user:password@localhost/dbname')
        self.metadata = MetaData()
        self.emails = Table('emails', self.metadata,
                            Column('id', Integer, primary_key=True),
                            Column('email', String(255), nullable=False),
                            Column('source_url', String(255), nullable=False),
                            Column('timestamp', DateTime, default=datetime.utcnow))

        self.metadata.create_all(self.engine)

    def save_email(self, email, source_url):
        with self.engine.connect() as connection:
            ins_query = self.emails.insert().values(email=email, source_url=source_url)
            connection.execute(ins_query)