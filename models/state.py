#!/usr/bin/python3
<<<<<<< HEAD
"""defines the State class."""
import models
from os import getenv
from models.base_model import Base
from models.base_model import BaseModel
from models.city import City
from sqlalchemy import Column
from sqlalchemy import String
=======
""" holds class State"""
import models
from models.base_model import BaseModel, Base
from models.city import City
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
>>>>>>> 4986009a09db768ae31339043b8ce5258d2d6d9f
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
<<<<<<< HEAD
    """represents a state for a MySQL database.

    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City",  backref="state", cascade="delete")

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """get a list of all related City objects."""
            city_list = []
            for city in list(models.storage.all(City).values()):
=======
    """Representation of state """
    if models.storage_t == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)

    if models.storage_t != "db":
        @property
        def cities(self):
            """getter for list of city instances related to the state"""
            city_list = []
            all_cities = models.storage.all(City)
            for city in all_cities.values():
>>>>>>> 4986009a09db768ae31339043b8ce5258d2d6d9f
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
