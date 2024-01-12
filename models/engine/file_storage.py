#!/usr/bin/python3
"""Define the FileStorage class"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """Represent the storage engine for the project
    Attribute:
        __file_path (str): the name of the file to save object
        __objects (dict): dictionary to instantiate the object
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        o_dict = FileStorage.__objects
        obj_dict = {key: value for key, value in o_dict.items()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists"""
        try:
            with open(FileStorage.__file_path, "r") as f:
                obj_dict = json.load(f)
            for key, value in obj_dict.items():
                cls_name = value["__class__"]
                cls_dict = {"BaseModel": BaseModel, "User": User, "State": State,
                        "City": City, "Amenity": Amenity, "Place": Place, "Review": Review}
                self.__objects[key] = cls_dictclsname
        except FileNotFoundError:
            pass
