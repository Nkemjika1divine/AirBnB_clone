#!/usr/bin/python3
"""This module contains the file_storage class"""
import os
import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """This is a FileStorage class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """This returns the objects attribute"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj value with class.id"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """This serializes or enters object to the json file"""
        with open(FileStorage.__file_path, "w") as f:
            obj = {}  # empty doctionary
            obj.update(FileStorage.__objects)
            for key, value in obj.items():
                if isinstance(value, BaseModel):
                    obj[key] = value.to_dict()
            json.dump(obj, f)

    def reload(self):
        """This deserializes json strings from files into __objects"""
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as f:
                try:
                    obj = json.load(f)
                    # parse through the files
                    for key, value in obj.items():
                        # split key into classname and id so you can use key
                        name_of_class, obj_id = key.split('.')
                        # evaluate the class name to get a reference to it
                        cls = eval(name_of_class)
                        # assign keyword arguments using the values
                        # tbis uses the cls instane to achieve that
                        new_obj = cls(**value)
                        # now add the new object to the __objects dictionary
                        self.new(new_obj)
                except Exception as E:
                    pass
