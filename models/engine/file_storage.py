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
        all_obj_dict = {}
        for key, obj in o_dict.items():
            obj_dict = {key: obj.to_dict()}
            all_obj_dict.update(obj_dict)
        with open(FileStorage.__file_path, "w") as f:
            json.dump(all_obj_dict, f)

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists"""
        try:
            with open(FileStorage.__file_path, "r") as f:
                obj_dict = json.load(f)
                
                for key, obj in obj_dict.items():
                    cls_name = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(cls_name)(**obj))
        except FileNotFoundError:
            pass
