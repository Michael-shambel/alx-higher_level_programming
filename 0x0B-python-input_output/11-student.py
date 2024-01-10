#!/usr/bin/python3
"""this define student class"""


class Student:
    """represent class"""

    def __init__(self, first_name, last_name, age):
        """ this inirialize new student
        args:
        first_name: name of first student
        last_name: last name of student
        age: age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """dictionart representation of a student"""
        if attrs is None:
            return self.__dict__
        return {attr: getattr(
            self, attr) for attr in attrs if hasattr(self, attr)}

    def reload_from_json(self, json):
        """replace the attribute"""
        for key, value in json.items():
            setattr(self, key, value)
