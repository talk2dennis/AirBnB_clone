#!/usr/bin/python3
"""
Method of init, a python model
importing the fileStorage model
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
