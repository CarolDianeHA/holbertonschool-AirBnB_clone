#!/usr/bin/python3
"""Class FileStorage."""

import json
import os
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.user import User
from models.review import Review


class FileStorage:
    """Class attributes: path and dictionary objects."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return dictionary."""
        return self.__objects

    def new(self, obj):
        """Set the object with key."""
        key = obj.__class__.__name__ + '.' + obj.id
        self.__objects[key] = obj

    def save(self):
        """Serialize objects to the Json file."""
        objects_dict = {}

        for key, value in self.__objects.items():
            objects_dict[key] = value.to_dict()

        with open(self.__file_path, mode='w', encoding='utf-8') as file:
            for key, value in self.__objects.items():
                objects_dict[key] = value.to_dict()
            json.dump(objects_dict, file, indent=2)

    def reload(self):
        """Deserialize the json file."""
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, mode='r', encoding='utf-8') as file:
                load = file.read()
                new_dict = json.loads(load)
                for key, value in new_dict.items():
                    self.__objects[key] = eval(value["__class__"])(**value)
