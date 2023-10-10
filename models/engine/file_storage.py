#!/usr/bin/python3
"""This module contains the file_storage class"""
from models.base_model import BaseModel


class FileStorage:
    """This is a FileStorage class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """This returns the objects attribute"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj value with class.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        # for obj.id, we assumr that he object passed to this method has an id
        # whether it is an object of BaseModel or another class
        FileStorage.__objects[key] = key
