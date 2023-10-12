#!/usr/bin/python3
"""This is a module containinf the city class"""
from models.base_model import BaseModel


class City(BaseModel):
    """This is a City Class that inherits from BaseModel """
    state_id = ""
    name = ""
