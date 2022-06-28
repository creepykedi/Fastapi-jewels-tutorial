from sqlmodel import create_engine
from sqlmodel import Session
eng = 'database.db'

sqlite_url = f'sqlite:///{eng}'
engine = create_engine(sqlite_url, echo=True)
session = Session(bind=engine)
