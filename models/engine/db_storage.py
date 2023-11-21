from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from os import getenv

class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(getenv('HBNB_MYSQL_USER'),
                                             getenv('HBNB_MYSQL_PWD'),
                                             getenv('HBNB_MYSQL_HOST'),
                                             getenv('HBNB_MYSQL_DB')), pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        session = self.__session
        if cls:
            objs = session.query(eval(cls)).all()
        else:
            objs = []
            for c in classes:
                objs += session.query(c).all()
        return {'{}.{}'.format(type(obj).__name__, obj.id): obj for obj in objs}

    def new(self, obj):
        session = self.__session
        session.add(obj)

    def save(self):
        session = self.__session
        session.commit()

    def delete(self, obj=None):
        session = self.__session
        if obj:
            session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(bind=self.__engine,
                                              expire_on_commit=False))
        self.__session = Session()
