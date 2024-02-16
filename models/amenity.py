#!/usr/bin/python3
""" Amenity module that defines the Amenity class """

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity - Defines the Amenity class that inherits from the BaseModel class
    Attributes:
        name: string - empty string
    """
    name = ""
