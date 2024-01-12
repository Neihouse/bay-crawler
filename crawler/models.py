from sqlalchemy import Column, String, Integer, DateTime, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class EmailRecord(Base):
    __tablename__ = 'email_records'

    id = Column(Integer, primary_key=True)
    email = Column(String(255), nullable=False)
    source_url = Column(String(2048), nullable=False)
    timestamp = Column(DateTime, default=func.now())

    def __repr__(self):
        return f"<EmailRecord(email='{self.email}', source_url='{self.source_url}')>"