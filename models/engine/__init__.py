#!/usr/bin/python3
""" initialization file """

import os
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage

HBNB_TYPE_STORAGE = os.environ.get('HBNB_TYPE_STORAGE')

if HBNB_TYPE_STORAGE == 'db':
    storage = DBStorage()
else:
    storage = FileStorage()

storage.reload()

