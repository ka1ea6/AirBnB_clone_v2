#!/usr/bin/env python3
"""This module defines a class to manage file storage for hbnb clone"""

from os import getenv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base, BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


env = getenv("HBNB_ENV")
user_name = getenv("HBNB_MYSQL_USER")
passwd = getenv("HBNB_MYSQL_PWD")
host_name = getenv("HBNB_MYSQL_HOST")
db_name = getenv("HBNB_MYSQL_DB")

classes = {"State": State, "City": City, "User": User,
           "Place": Place, "Review": Review, "Amenity": Amenity}


class DBStorage:
    '''Class for managing storage using a database'''

    __engine = None
    __session = None

    def __init__(self):
        '''initialize instances'''
        self.__engine = create_engine(f"mysql+mysqldb:\
//{user_name}:{passwd}@{host_name}:3306/{db_name}", pool_pre_ping=True)

        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        '''query on the current database session all objects
        depending on the class name'''

        result = {}
        if cls:
            if isinstance(cls, str) and cls in classes:
                query = self.__session.query(classes[cls]).all()
                for instance in query:
                    result[f"{instance.__class__.__name__}.{instance.id}"] = instance
            elif cls.__name__ in classes:
                query = self.__session.query(cls).all()
                for instance in query:
                    result[f"{instance.__class__.__name__}.{instance.id}"] = instance

        else:
            for to_fetch in classes.values():
                result = {**result, **self.all(to_fetch)}

        return result

    def new(self, obj):
        '''Add the object to the current database session'''
        if obj:
            self.__session.add(obj)

    def save(self):
        '''Commit all changes of the current database session'''
        self.__session.commit()

    def delete(self, obj=None):
        '''delete from the current database session'''
        if obj:
            self.__session.delete(obj)

    def reload(self):
        '''create all tables in the database'''
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)

        self.__session = Session()

    def close(self):
        '''Method used for removing element'''
        self.__session.remove()