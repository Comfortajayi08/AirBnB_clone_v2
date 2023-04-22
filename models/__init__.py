#!/usr/bin/python3
"""This module instantiates an object of Dbstorage if it exists
or filestorage if it doesnt exist"""

from models.engine.file_storage import FileStorage
from os import getenv
from models.engine.db_storage import DBStorage

if getenv('HBNB_TYPE_STORAGE') == 'db':
    storage = DBStorage()
else:
    storage = FileStorage()
storage.reload()
