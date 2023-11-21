from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base_model import Base
from models.state import State
from models.city import City
import os

# Set up database engine
engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                       format(os.getenv('HBNB_MYSQL_USER'),
                              os.getenv('HBNB_MYSQL_PWD'),
                              os.getenv('HBNB_MYSQL_HOST'),
                              os.getenv('HBNB_MYSQL_DB')), pool_pre_ping=True)

# Create tables
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()
