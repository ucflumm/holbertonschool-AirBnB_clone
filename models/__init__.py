"""
    From task 5:
    Update models/__init__.py: to create a unique FileStorage instance
    for your application

        import file_storage.py
        create the variable storage, an instance of FileStorage
        call reload() method on this variable

    This module instantiates an object of class FileStorage
"""
from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()