#!/usr/bin/python3
"""Defines FileStorage class"""

import imp
import json
import os
from models.base_model import BaseModel
from models.user import User


class FileStorage():
    """Serializes instances to a JSON file and
    deserializes JSON file to instances"""
    __file_path = "file.json"
    __objects = dict()

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        dic = self.__objects.copy()
        for k, v in dic.items():
            dic[k] = v.to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(dic, f)

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON
        file (__file_path) exists ; otherwise, do nothing. If the file
        doesn’t exist, no exception should be raised)"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r") as f:
                for obj in json.load(f).values():
                    instance = eval(obj["__class__"])(**obj)
                    self.new(instance)
