from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DataStorage:
    def __init__(self):
        self.engine = create_engine('mysql+pymysql://user:password@localhost/dbname')
        self.Session = sessionmaker(bind=self.engine)

    def save_email(self, company_name, email, source_url, timestamp):
        # This method will save the extracted email to the database
        # It will be implemented later
        pass