#!/usr/bin/python3

"""A module that contains code to create a unique storage """

from models.engine.file_storage import FileStorage
from os import getenv
from models.city import City
from models.amenity import Amenity
from models.engine.db_storage import DBStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.place import Place
from models.review import Review


if getenv("HBNB_TYPE_STORAGE") == "db":
    storage = DBStorage()

else:
    storage = FileStorage()
storage.reload()
