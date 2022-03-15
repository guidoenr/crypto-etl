from configparser import ConfigParser
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def config(filename='database.ini', section='postgresql'):
    parser = ConfigParser()
    parser.read(filename)
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))
    return db

def get_engine_and_session():
    params = config()
    db_uri = 'postgresql+psycopg2://{user}:{password}@{host}/{database}'.format(**params)
    engine = create_engine(db_uri, echo=True)
    Session = sessionmaker(engine)
    return engine, Session()

