from sqlalchemy import create_engine, and_
from sqlalchemy.orm import sessionmaker
import config

def connent(db = config.DATABASE_URL):
    """
    数据库连接
    """
    engine = create_engine(db)
    Session = sessionmaker(bind=engine, autoflush=False)
    db = Session()

    return db, engine, Session