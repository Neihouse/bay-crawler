from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class EmailItem(Base):
    __tablename__ = 'email_items'
    id = Column(Integer, primary_key=True)
    company_name = Column(String(255))
    email = Column(String(255), unique=True)
    source_url = Column(String(255))
    timestamp = Column(DateTime, default=datetime.utcnow)