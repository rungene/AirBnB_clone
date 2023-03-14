<<<<<<< HEAD
#!/usr/bin/python3
"""
@authors: Clevers Rungene
          Lawrence Ongaki

    File Storage Module
"""
from models.base_model import BaseModel
import json


class FileStorage:
    """
    FileStorage class for serialization/deserialization objects
    into and from files.

    Attributes:
        __file_path(string) - path to the JSON file
        __objects (dictionary) - empty but will store all
        objects by <class name>.id
         (ex: to store a BaseModel object with id=12121212,
         the key will be BaseModel.12121212)
    """
    __file_path = 'file.json'
    __objects = dict()

    def __init__(self):
        """Init method for file storage class"""
        pass

    def all(self):
        """public instance method
        Return:
             returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id

        Attributes:
            obj(Python object): The object to set
        """
        dictionary = obj.to_dict()
        key = '{}.{}'.format(dictionary['__class__'], str(obj.id))
        FileStorage.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        dictionary = dict()
        for k, v in FileStorage.__objects.items():
            dictionary[k] = v.to_dict()
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            json.dump(dictionary, file)

    def reload(self):
        """
        deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists ; otherwise, do nothing. If the file doesn’t
        exist, no exception should be raised)
        """
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                json_load = json.load(file)
            for k, v in json_load.items():
                FileStorage.__objects[k] = BaseModel(**v)
        except Exception:
=======
import json
import os
from models.base_model import BaseModel


class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON file to
            instances."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        obj_dict = {}
        for key, value in self.__objects.items():
            obj_dict[key] = value.to_dict()
        with open(self.__file_path, mode='w', encoding='utf-8') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        try:
            with open(self.__file_path, mode='r', encoding='utf-8') as f:
                obj_dict = json.load(f)
                for key, value in obj_dict.items():
                    cls_name, obj_id = key.split('.')
                    cls = getattr(models, cls_name)
                    obj = cls(**value)
                    self.__objects[key] = obj
        except FileNotFoundError:
>>>>>>> master
            pass
