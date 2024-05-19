#!usr/bin/python3
"""Module file_storage"""

import json


class FileStorage:
    """
    Serializes instances to a JSON file and
    deserializes JSON file to instances.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return type(self).__objects

    def new(self, obj):
        """Sets in __objects the obj with the key <obj class name>.id"""
        obj_key = "{}.{}".format(type(obj).__name__, obj.id)
        type(self).__objects[obj_key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        n_dict = {}
        n_dict.update(type(self).__objects)

        for item in n_dict.keys():
            n_dict[item] = n_dict[item].to_dict()

        json_str = json.dumps(n_dict)

        with open(type(self).__file_path, "w") as file:
            file.write(json_str)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists; otherwise, do nothing
        """
        from models.base_model import BaseModel
        from models.user import User

        try:
            with open(type(self).__file_path, "r", encoding="utf-8") as file:
                json_str = file.read()

            n_dict = json.loads(json_str)
            for key, value in n_dict.items():
                classname = key.split(".")[0]
                if classname == "BaseModel":
                    inst = BaseModel(**value)
                elif classname == "User":
                    inst = User(**value)
                type(self).__objects[key] = inst
        except FileNotFoundError:
            pass
