#!/usr/bin/python3
"""Module: base_model.py"""
import uuid
from datetime import datetime
from models import engine
from models import storage



class BaseModel:
    """Define BaseModel calss"""

    def __init__(self, *args, **kwargs):
        """Initiate instance var"""
        if len(kwargs) > 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    v = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                    self.__setattr__(k, v)
                elif k != "__class__":
                    self.__setattr__(k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Print string value of class"""
        return f"[{type(self).__name__}] ({self.id}) {self.to_dict()}"

    # Pbulic instance methods
    def save(self):
        """ Updates date and time """
        self.updated_at = datetime.now()
        # from task 5: update models/base_model.py to link BaseModel
        # to FileStorage. That currently works but it also asks to add
        # init method to FileStorage class. I've commented it out for now
        # __init__(self, *args, **kwargs)
        storage.new(self)
        storage.save()


    def to_dict(self):
        """Return a dictionary format of instance"""
        # dictionary is mutable, make a copy to avoid value being changed
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = type(self).__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
