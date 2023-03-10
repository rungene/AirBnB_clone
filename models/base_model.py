# simple task-3 BaseModel. All other work => branches

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
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key != '__class__':
                    setattr(self, key, value)
            self.id = kwargs.get('id', str(uuid.uuid4()))
            self.created_at = kwargs.get('created_at', datetime.now())
            self.updated_at = kwargs.get('updated_at', datetime.now())
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

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
        self.updated_at = datetime.now()

    def to_dict(self):
        """defined to convert the instance to a dictionary representation."""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
