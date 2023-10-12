#!/usr/bin/python3
"""This module houses the BaseModel class"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """This is the Base class for all the packages"""

    def __init__(self, *args, **kwargs):
        """This is the instantiation phase"""
        from models.__init__ import storage
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key == 'created_at' or key == 'updated_at':
                    setattr(
                        self,
                        key,
                        datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    )
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()  # sets a creatioj time
            self.updated_at = datetime.now()  # sets a creation time as well
            storage.new(self)

    def save(self):
        """This updates updated_at with the current datetime"""
        from models.__init__ import storage
        self.updated_at = datetime.now()  # Updates the new time
        storage.save()

    def to_dict(self):
        """Returns a dictionary containing keys/values of __dict__ of inst"""
        dict_obj = self.__dict__.copy()  # copies the dictionary
        dict_obj['__class__'] = self.__class__.__name__
        # Previous line creates a class key
        dict_obj['created_at'] = self.created_at.isoformat()
        dict_obj['updated_at'] = self.updated_at.isoformat()
        # The two lines create a updated_at and created_at key
        # It also uses the isoformat() method to create that
        return dict_obj

    def __str__(self):
        """This is a string representation of the basemodel class"""
        return "[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id,
            self.__dict__
        )
