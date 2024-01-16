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

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""

        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new_inst = cls(1, 1)
            else:
                new_inst = cls(1)
            new_inst.update(**dictionary)
            return new_inst

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""

        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as f:
                json_string = f.read()
                dictionaries = cls.from_json_string(json_string)
                file_instances = [cls.create(**d) for d in dictionaries]
                return file_instances
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV representation of list_objs to a file."""
        filename = cls.__name__ + ".csv"
        with open(filename, "w") as f:
            if list_objs is not None:
                for obj in list_objs:
                    if cls.__name__ == "Rectangle":
                        f.write(f"{obj.id},{obj.width},{obj.height},{obj.x},{obj.y}\n")
                    elif cls.__name__ == "Square":
                        f.write(f"{obj.id},{obj.size},{obj.x},{obj.y}\n")

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of instances loaded from a CSV file."""
        filename = cls.__name__ + ".csv"
        instances = []
        try:
            with open(filename, "r") as f:
                for line in f:
                    values = line.strip().split(',')
                    if cls.__name__ == "Rectangle":
                        from models.rectangle import Rectangle
                        instance = Rectangle(int(values[0]), int(values[1]), int(values[2]), int(values[3]), int(values[4]))
                    elif cls.__name__ == "Square":
                        from models.square import Square
                        instance = Square(int(values[0]), int(values[1]), int(values[2]), int(values[3]))
                    instances.append(instance)
        except FileNotFoundError:
            pass
        return instances
