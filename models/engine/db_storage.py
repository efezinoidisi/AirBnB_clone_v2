#!/usr/bin/python3

"""
This module contains the DBStorage class which
is the database engine
"""
from models.base_model import Base
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from os import getenv

user = getenv("HBNB_MYSQL_USER")
passwd = getenv("HBNB_MYSQL_PWD")
host = getenv("HBNB_MYSQL_HOST")
db = getenv("HBNB_MYSQL_DB")
env = getenv("HBNB_ENV")

DB = f"mysql+mysqldb://{user}:{passwd}@{host}/{db}"

class DBStorage:
    """This class defines the database engine"""
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine(DB, pool_pre_ping=True)

        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on the current database session
        all objects depending of the class name
        """
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = [State, City, User, Place, Review]
        dictionary = {}
        if cls:
            objs = self.__session.query(cls)
        else:
            for cls_name in classes:
                objs = self.__session.query(cls_name)

                for obj in objs:
                    key = f"{obj.__class__.__name__}.{obj.id}"
                    dictionary.update({key: obj})
        return dictionary

    def new(self, obj):
        """Add the object to the current db session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current db session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session obj if
        not None
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Creates all tables in the database"""
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(bind=self.__engine,
                                              expire_on_commit=True))
        self.__session = Session()
