#!/usr/bin/python3
"""
AirBnB clone - The console
File_storage module
"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.city import City


class FileStorage:
    """
    FileStorage - sterializes instances to a JSON file
                and deserializes JSON file to instances
    Args:
        __file_path: the path to store the objects
        __objects: a dict to store the objects
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns all the objects """
        return FileStorage.__objects

    def new(self, obj):
        """ stages an object for saving it to a file """
        name = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[name] = obj

    def save(self):
        """ saves the instance of an object to a file """
        with open(FileStorage.__file_path, "w") as f:
            serialized_objs = {key: value.to_dict() for key,
                               value in self.__objects.items()}
            json.dump(serialized_objs, f)

    def reload(self):
        """
        loads json objects from the file and returns the class instance
        """
        allowed_class = {
                "BaseModel": BaseModel,
                "User": User,
                "State": State,
                "City": City,
                "Place": Place,
                "Amenity": Amenity,
                "Review": Review
                }
        try:
            with open(FileStorage.__file_path, "r") as f:
                obj_dict = json.loads(f.read())
                FileStorage.__objects = {
                                         key: allowed_class[key.split('.')[0]]
                                         (**value) for key, value in
                                         obj_dict.items()}
        except Exception:
            pass
