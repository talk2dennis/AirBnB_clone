#!/usr/bin/python3
""" City module that defines the City class """

from models.base_model import BaseModel


class City(BaseModel):
    """
    City - Defines the City class that inherits from the BaseModel class
    Attributes:
        name: string - empty string
        state_id: string - empty string: it will be the State.id
    """
    name = ""
    state_id = ""
