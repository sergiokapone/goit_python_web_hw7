import configparser
from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#  postgresql://username:password@host:port/database_name
file_config = Path(__file__).parent.parent.joinpath('config.ini')
config = configparser.ConfigParser()
config.read(file_config)

user_name = config.get('DB', 'USER')
password = config.get('DB', 'PASSWORD')
database_name = config.get('DB', 'DB_NAME')
domain = config.get('DB', 'DOMAIN')
port= config.get('DB', 'PORT')

url = f'postgresql://{user_name}:{password}@{domain}:{port}/{database_name}'

engine = create_engine(url, echo=False)
DBSession = sessionmaker(bind = engine)
session = DBSession()