#!/usr/bin/python3
"""Module holds the Class which represent a database storage system for our
    application, which wrap all method we need
"""

from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv


class DBStorage:
    """Class that represent a database storage system for our
    application, which wrap all method we need
    """

    __engine = None
    __session = None

    def __init__(self):
        """
        Init and create the engine and all models
        """

        from models.base_model import Base
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                getenv('HBNB_MYSQL_USER'),
                getenv('HBNB_MYSQL_PWD'),
                getenv('HBNB_MYSQL_HOST'),
                getenv('HBNB_MYSQL_DB')))

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Return all the records, or specific class
        """
        from models.amenity import Amenity
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.review import Review

        classes = [Amenity, User, Place, State, City, Review]
        # classes = [State, City]
        if cls:
            objs = self.__session.query(cls)
        else:
            objs = []
            for c in classes:
                objs += self.__session.query(c)

        return {'{}.{}'.format(type(obj).__name__, obj.id):
                obj for obj in objs}

    def reload(self):
        """
        Create all tables and generate our session
        """

        from models.base_model import Base
        from models.amenity import Amenity
        from models.place import Place
        from models.user import User
        from models.state import State
        from models.review import Review
        from models.city import City

        Base.metadata.create_all(self.__engine)

        DBStorage.Session = scoped_session(
            sessionmaker(bind=self.__engine, expire_on_commit=False))

        self.__session = DBStorage.Session()

    def new(self, obj):
        """
        Add new or edited object to the session
        """
        if obj in self.__session:
            _obj = self.__session.merge(obj)
        else:
            self.__session.commit()
            self.__session.add(obj)

    def delete(self, obj=None):
        """
        Delete the obj object from the session
        if its already there
        """
        if obj and obj in self.__session:
            self.__session.delete(obj)

    def save(self):
        """
        Commit all changes or update on the session
        """
        self.__session.commit()

    def close(self):
        """
        Close the connection between the database system and the application
        """
        self.__session.close()
