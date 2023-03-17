#!/usr/bin/python3
"""Class BaseModel."""

from uuid import uuid4
from datetime import datetime
import json
import models


class BaseModel:
    """Class that defines all common attributes/methods for other classes."""

    def __init__(self, *args, **kwargs):
        """Instances of the base model class.
        Args:
            id: unique identification.
            created_at: datetime - datetime when an instance is created.
            updated_at: datetime - datetime when an instance is modified.
        """
        timeformat = "%Y-%m-%dT%H:%M:%S.%f"
        if len(kwargs) != 0:
            for key, val in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(val, timeformat))
                elif key != '__class__':
                    setattr(self, key, val)

        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Print class name, id, and dictionary representation."""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """Update attribute with the current datetime."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return dictionary representation of the instance's attributes."""
        dict = self.__dict__.copy()
        dict['__class__'] = self.__class__.__name__
        dict['created_at'] = self.created_at.isoformat()
        dict['updated_at'] = self.updated_at.isoformat()
        return dict
