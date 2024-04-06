#!/usr/bin/python3

"""A module with the file storage class for AirBnB"""

import json
from models.state import State
from models.amenity import Amenity
import shlex
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.review import Review


class FileStorage:
    """A class that serializes instances to a JSON file and
    deserializes JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """returns a dictionary"""

        _dictionary = {}
        if cls:
            dictionary = self.__objects

            for key in dictionary:
                partition = key.replace('.', ' ')
                partition = shlex.split(partition)

                if (partition[0] == cls.__name__):
                    _dictionary[key] = self.__objects[key]
            return (_dictionary)

        else:
            return self.__objects

    def new(self, obj):
        """sets __object to given obj"""

        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """A fn that serialize the file path to JSON file path"""

        custom_dict = {}
        for key, value in self.__objects.items():
            custom_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(custom_dict, f)

    def reload(self):
        """A fn that serialize the file path to JSON file path"""

        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                for key, value in (json.load(f)).items():
                    value = eval(value["__class__"])(**value)
                    self.__objects[key] = value
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """A fn that delete an existing element"""

        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            del self.__objects[key]

    def close(self):
        """A fn that calls reload()"""

        self.reload()
