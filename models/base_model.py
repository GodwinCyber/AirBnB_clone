#!/usr/bin/python3
"""Define the BaseModel class"""

import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Rep the BaseModel of the HBnB project"""

    def __init__(self, *args, **kwargs):
        """Initialise the new BaseModel"""
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

        if kwargs:
            for k, v in kwargs.items():
                if k in ["created_at", "updated_at"]:
                    self.__dict__[k] = datetime.strptime(v, tform)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def save(self):
        """update the update_at with current datetime"""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """
            Return the dictionary of the BaseModel instance
            returns a dictionary containing all keys/values
            of __dict__ of the instance
        """
        result = self.__dict__.copy()
        result["created_at"] = self.created_at.isoformat()
        result["updated_at"] = self.updated_at.isoformat()
        result["__class__"] = self.__class__.__name__
        return result

    def __str__(self):
        """return the str Representation of the BaseModel"""
        callname = self.__class__.__name__
        return "[{}] ({}) {}".format(callname, self.id, self.__dict__)
