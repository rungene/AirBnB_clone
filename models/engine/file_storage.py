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
        __file_path-string - path to the JSON file
        __objects -  dictionary - empty but will store all
        objects by <class name>.id
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
        key = '{}{}'.format(dictinary['__class__'], str(obj.id))
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
            pass
