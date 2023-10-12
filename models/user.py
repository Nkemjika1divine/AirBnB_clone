#!/usr/bin/python3
"""This is the User Module"""
from models.base_model import BaseModel


class User(BaseModel):
    """This is the user class that inherits from BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
