#!/usr/bin/python3

"""Module containing the base model class for AirBnB"""

import uuid
import models
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime


Base = declarative_base()


class BaseModel:
    """A class defining common attributes for other classes"""

    id = Column(String(60), unique=True, nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=(datetime.utcnow()))
    updated_at = Column(DateTime, nullable=False, default=(datetime.utcnow()))

    def __init__(self, *args, **kwargs):
        """Instantiates the base model class"""

        if kwargs:
            for key, val in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    val = datetime.strptime(val, "%Y-%m-%dT%H:%M:%S.%f")

                if key != "__class__":
                    setattr(self, key, val)

            if "id" not in kwargs:
                self.id = str(uuid.uuid4())

            if "created_at" not in kwargs:
                self.created_at = datetime.now()

            if "updated_at" not in kwargs:
                self.updated_at = datetime.now()

        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """Returns a string representation of the object"""

        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def __repr__(self):
        """Returns a string representation of the object"""

        return self.__str__()

    def save(self):
        """Updates the updated_at attribute to the current datetime"""

        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Creates a dictionary representation of the class"""

        custom_dict = dict(self.__dict__)
        custom_dict["__class__"] = str(type(self).__name__)
        custom_dict["created_at"] = self.created_at.isoformat()
        custom_dict["updated_at"] = self.updated_at.isoformat()
        if '_sa_instance_state' in custom_dict.keys():
            del custom_dict['_sa_instance_state']
        return custom_dict

    def delete(self):
        """Deletes the object"""

        models.storage.delete(self)
