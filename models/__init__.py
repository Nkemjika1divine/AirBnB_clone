#!/usr/bin/python3
"""This is used to create a storage instance from the FileStorage class"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
