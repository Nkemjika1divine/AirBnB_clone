#!/usr/bin/python3
"""This is a module containing the Review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """This is a Review Class that inherits from BaseModel"""
    place_id = ""
    user_id = ""
    text = ""
