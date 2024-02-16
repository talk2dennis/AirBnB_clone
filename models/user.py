#!/usr/bin/python3
""" user class module thant defines the attributes """

from models.base_model import BaseModel


class User(BaseModel):
    """
    User - that inherits from BaseModel
    Args:
        email: string - empty string
        password: string - empty string
        first_name: string - empty string
        last_name: string - empty string
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
