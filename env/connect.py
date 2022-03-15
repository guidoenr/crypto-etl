from configparser import ConfigParser
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def config(filename='db.ini', section='psql'):
    parser = ConfigParser()
    parser.read(filename)
    db = {}
    params = parser.items(section)
    for param in params:
        db[param[0]] = param[1]
    return db

def get_engine_and_session():
    params = config()
    db_uri = 'postgresql+psycopg2://{user}:{password}@{host}'.format(**params)
    engine = create_engine(db_uri, echo=True)
    conn = engine.connect()
    conn.execute("commit")
    conn.execute("create database crypto")
    conn.close()
    Session = sessionmaker(engine)
    return engine, Session()

