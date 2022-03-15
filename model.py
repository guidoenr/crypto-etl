from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, String, DateTime, Integer, JSON, ForeignKey
from sqlalchemy_utils import database_exists, create_database
from datetime import datetime
from env import connect


Base = declarative_base()
engine, session = connect.get_engine_and_session()


class CoinDB(Base):
    __tablename__='coin'
    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(6), nullable=False)
    year = Column(String, nullable=False)
    month = Column(String, nullable=False)
    max_price = Column(Integer, nullable=False)
    min_price = Column(Integer, nullable=False)
    


def init():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


if __name__ == '__main__':
    init()