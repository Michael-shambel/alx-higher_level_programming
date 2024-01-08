#!/usr/bin/python3
""" define base geometry"""


class BaseGeometry:
    """ base geometry class"""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ check (validate) parameter as integer
        check the value argument is integer and greater than zero"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
