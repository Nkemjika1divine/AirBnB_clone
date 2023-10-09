#!/usr/bin/python3
"""This module houses the BaseModel class"""
from uuid import uuid4
from cmd import Cmd
from datetime import datetime


class BaseModel:
    """This is the Base class for all the packages"""
    self.id = str(uuid4())
    created_at = datetime.now()
    updated_at = datetime.now()

    def save(self):
        """This updates updated_at with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing keys/values of __dict__ of inst"""


    def __str__(self):
        """This is a string representation of the basemodel class"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
