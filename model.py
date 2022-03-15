from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, String, DateTime, Integer, JSON, ForeignKey
from datetime import datetime
import connect


Base = declarative_base()
engine, session = connect.get_engine_and_session()

# pareciera que el error es porque ya esta creado, no hace falta crearlo denuveo? TODOa
class Coin(Base):
    __tablename__='coin'
    id = Column(Integer, nullable=False, primary_key=True)
    coin_id = Column(String(6), nullable=False)
    price_usd = Column(Integer, nullable=False)
    date = Column(DateTime, default=datetime.now().strftime("%d-%m-%Y"))
    json = Column(JSON, nullable=False)
    


class CoinData(Base):
    __tablename__='coin_data'
    id = Column(Integer, primary_key=True)
    coin_id = Column(String)
    year = Column(String(4), nullable=False)
    month = Column(String(2), nullable=False)
    max_price = Column(Integer, nullable=False)
    min_price = Column(Integer, nullable=False)



def init():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


if __name__ == '__main__':
    init()