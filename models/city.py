#!/usr/bin/python3

"""Module containing the City class"""

from sqlalchemy.ext.declarative import declarative_base
from models.place import Place
from sqlalchemy import Column, Integer, String
from models.base_model import BaseModel, Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """A class representing a city"""

    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    places = relationship("Place", cascade='all, delete, delete-orphan',
                          backref="cities")