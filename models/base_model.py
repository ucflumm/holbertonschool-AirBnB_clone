#!/usr/bin/python3
"""
    Module: base_model.py
"""
from datetime import datetime


class BaseModel:
    """
        Definition of BaseModel class 
        
        Functions:

        Attributes:
    """
    def __init__(self, id, created_at, updated_at)
    """
        Parameterized constructed:
        
        id: is initialized with uuid
        created_at: datetime - assign current datetime
        updated_at: datetime - assign current datetime synced with creation
    """
        id = str(uuid.uuid(4))
        created_at = datetime.now()
        updated_at = created_at
    
    def __str__(self):
        """ string representation of BaseModel """
        return "[{}] ({}) {}".format(type(self).__nabase_model.py

    # Pbulic instance methods
    def save(self):
        """ Updates date and time """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ returns a dictionary definition containing all keys/values of __dict__ instance """
        # TODO
    



