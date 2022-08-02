#!/usr/bin/python3
"""Defines BaseModel class"""

from uuid import uuid4
from datetime import datetime
import models


class BaseModel():
    """Defines all common attributes/methods for other classes"""
    def __init__(self, *args, **kwargs):
        """Instanciation of class"""
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ["created_at", "updated_at"]:
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)

    def __str__(self):
        """Return description of instance"""
        return "{} ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates the public instance attribute updated_at with
        the current datetime"""
        setattr(self, "updated_at", datetime.now())
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values
        of __dict__ of the instance:"""
        dico = self.__dict__.copy()
        dico["__class__"] = self.__class__.__name__
        dico["updated_at"] = dico["updated_at"].isoformat()
        dico["created_at"] = dico["created_at"].isoformat()
        return dico
