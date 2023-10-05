#!/usr/bin/python3
<<<<<<< HEAD
"""instantiates a storage object.

"""
from os import getenv


if getenv("HBNB_TYPE_STORAGE") == "db":
=======
"""
initialize the models package
"""

from os import getenv


storage_t = getenv("HBNB_TYPE_STORAGE")

if storage_t == "db":
>>>>>>> 4986009a09db768ae31339043b8ce5258d2d6d9f
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
