#!/usr/bin/python3
"""Module base_model"""

from datetime import datetime
import uuid


class BaseModel():
    """Defines all common attributes/methods for other classes"""
    def __init__(self):
        """Initialize BaseModel class"""
        self.id = str(uuid.uuid4())  # random unique id using uuid4
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Informal string representation of BaseModel class"""
        return "[{:s}] ({:s}) {}" \
            .format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates the public instance attribute updated_at
        with the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of
        __dict__ of the instance.
        """
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = dictionary['created_at'].isoformat()
        dictionary['updated_at'] = dictionary['updated_at'].isoformat()
        return dictionary
