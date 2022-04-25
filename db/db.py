from sqlmodel import create_engine
from sqlmodel import Session
eng = r'\Users\Evgeny\PycharmProjects\jewels\database.db'
sqlite_url = f'sqlite:///{eng}'
engine = create_engine(sqlite_url, echo=True)
session = Session(bind=engine)
