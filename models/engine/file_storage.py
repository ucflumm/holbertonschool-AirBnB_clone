#!/usr/bin/python3
"""Module: file_storage.py"""
import json
import uuid
from datetime import datetime


class FileStorage:
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        with open(self.__file_path, 'w') as f:
            data = {key: obj.to_dict() for key, obj in self.__objects.items()}
            json.dump(data, f)

    def reload(self):
        from models.base_model import BaseModel
        try:
            with open(self.__file_path, 'r') as f:
                data = json.load(f)

            for key, value in data.items():
                class_name = key.split('.')[0]

                if class_name in globals():
                    obj = globals()[class_name](**value)
                    self.__objects[key] = obj

        except FileNotFoundError:
            pass
