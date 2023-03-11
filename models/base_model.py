#!/usr/bin/python3
# Simple task-3 BaseModel. All other work => branches

"""
    Base Module
"""
import uuid
from datetime import datetime


class BaseModel:
    """Base class from where all other classes will inherit from"""
    def __init__(self, *args, **kwargs):
        """ initializes the instance with three public instance attributes
            : id, created_at, and updated_at.

            Attributes:
                id(string) - uuid when an instance is created
                created_at(datetime) - current datetime when
                an instance is created
                updated_at(datetime) - current datetime when
                an instance is created
                and it will be updated every time you change your object
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = save()

    def __str__(self):
        """ defined to return a string representation of the instance.
              It formats the string using the class name, id,
                and __dict__ attribute of the instance.
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__
                                     dict__)

    def save(self):
        """ defined to update the updated_at attribute of the instance with
                  the current datetime using the datetime.now() method."""
        return datetime.now()

    def to_dict(self):
        """defined to convert the instance to a dictionary representation.

           Return:
            obj_dict(dictionary): Dictionary object containing __dict__
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
