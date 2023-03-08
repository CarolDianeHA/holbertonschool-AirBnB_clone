#!/usr/bin/python3
"""Class BaseModel"""

import uuid
from datetime import datetime

# date format
dtm = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """Class that defines all common attributes/methods for other classes"""
    def __init__(self):
        """
        Initialization of the objects:
        id: unique identification
        created_at: datetime - datetime when an instance is created
        updated_at: datetime - datetime when an instance is modified
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Prints class name, id, and dictionary representation"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """Updates attribute with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns dictionary representation of the instance's attributes"""
        dict = self.__dict__.copy()
        dict['__class__'] = type(self).__name__
        return dict
