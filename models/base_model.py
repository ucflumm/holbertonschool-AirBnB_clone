#!/usr/bin/python3
"""Module: base_model.py"""
import uuid
from datetime import datetime


class BaseModel:
    """Define BaseModel calss"""

    def __init__(self):
        """Initiate instance var"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Print string value of class"""
        return f"[{type(self).__name__}] {self.id} {self.to_dict()}"

    # Pbulic instance methods
    def save(self):
        """ Updates date and time """
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return a dictionary format of instance"""
        # dictionary is mutable, make a copy to avoid value being changed
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = type(self).__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
