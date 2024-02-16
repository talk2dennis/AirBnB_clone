#!/usr/bin/python3
""" base model class """
import uuid
from datetime import datetime
import models


class BaseModel:
    """
        BaseModel - defines all common attributes/methods for other classes
        Args:
            id: string - assign with an uuid when an instance is created
            created_at: datetime - assign with the current datetime
                        when an instance is created
            updated_at: datetime - assign with the current datetime
                        when an instance is created and it will be updated
                        every time you change your object
    """

    def __init__(self, *args, **kwargs):
        """ initialises the BaseModel class parameters """
        date_format = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key in ("created_at", "updated_at"):
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = self.created_at
            models.storage.new(self)

    def save(self):
        """ function to save the object instance """
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """ converts the object attributes to dictionary """
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict

    def __str__(self):
        """ returns the dict representation of the class """
        name = self.__class__.__name__
        return "[{}] ({}) {}".format(name, self.id, self.__dict__)
