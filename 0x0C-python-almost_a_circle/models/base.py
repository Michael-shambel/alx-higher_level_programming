#!/usr/bin/python3
""" this is class of base """
import json


class Base:
    """ this class will clreae a private attribute"""

    __nb_objects = 0

    def __init__(self, id=None):
        """this is constracture methiod"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """return the JSON serialization of a list"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """write the JSON string of objs"""
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                diction = [obj.to_dictionary() for obj in list_objs]
                json_file = cls.to_json_string(diction)
                f.write(json_file)
