#!/usr/bin/python3
"""This is the file storage class for AirBnB"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from os import getenv

class DBStorage:
    """ DBStorage class """
    __engine = None
    __session = None

    def __init__(self):
        """ Initializes a new DBStorage instance """
        user = getenv('HBNB_MYSQL_USER')
        pwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')
        env = getenv('HBNB_ENV')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, pwd, host, db),
                                      pool_pre_ping=True)

        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Returns a dictionary of all objects """
        from models import State, City, User, Place, Review, Amenity

        classes = {"State": State, "City": City, "User": User,
                   "Place": Place, "Review": Review, "Amenity": Amenity}

        if cls:
            return {k: v for k, v in self.__session.query(cls).all()}

        return {k: v for cls in classes.values()
                for k, v in self.__session.query(cls).all()}

    def new(self, obj):
        """ Adds the object to the current database session """
        self.__session.add(obj)

    def save(self):
        """ Commits all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ Deletes an object from the current database session """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ Creates all tables in the database and creates a new session """
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)


