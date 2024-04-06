#!/usr/bin/python3

"""A module with the new class for sqlAlchemy"""

from os import getenv
from models.place import Place
from models.user import User
from models.city import City
from models.amenity import Amenity
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import (create_engine)
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import Base
from models.state import State
from models.review import Review


class DBStorage:
    """A class that create tables in environmental"""

    __engine = None
    __session = None

    def __init__(self):
        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        env = getenv("HBNB_ENV")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, passwd, host, db),
                                      pool_pre_ping=True)

        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """A fn that returns a dictionary"""

        _dictionary = {}
        if cls:
            if type(cls) is str:
                cls = eval(cls)
            query = self.__session.query(cls)

            for elements in query:
                key = "{}.{}".format(type(elements).__name__, elements.id)
                _dictionary[key] = elements

        else:
            lista = [State, City, User, Place, Review, Amenity]

            for clase in lista:
                query = self.__session.query(clase)

                for elements in query:
                    key = "{}.{}".format(type(elements).__name__, elements.id)
                    _dictionary[key] = elements

        return (_dictionary)

    def new(self, obj):
        """A fn that adds a new element in the table"""

        self.__session.add(obj)

    def save(self):
        """A fn that saves changes"""

        self.__session.commit()

    def delete(self, obj=None):
        """A fn that deletes an element in the table"""

        if obj:
            self.session.delete(obj)

    def reload(self):
        """A function with the configuration"""

        Base.metadata.create_all(self.__engine)
        sec = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sec)
        self.__session = Session()

    def close(self):
        """A function that calls remove()"""

        self.__session.close()
