from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from contextlib import contextmanager

engine = create_engine('mysql+pymysql://user:password@localhost/dbname')
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)

@contextmanager
def session_scope():
    """Provide a transactional scope around a series of operations."""
    session = Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()