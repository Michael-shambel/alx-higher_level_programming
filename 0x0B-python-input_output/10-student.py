#!/usr/bin/python3
"""define student class"""


class Student:
    """this class represent the student"""

    def __init__(self, first_name, last_name, age):
        """initialize to accept new student
        args:
        first_name: first name of the student
        last_name: last name of the student
        age: age of the student
        return:
        student information object
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """get the dictionary for the student"""

        if attrs is None:
            return self.__dict__
        return {attr: getattr(
            self, attr) for attr in attrs if hasattr(self, attr)}
