#!/usr/bin/python3
""" define a class of rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """rectangle using basegeometry"""

    def __init__(self, width, height):
        """initialie the rectangle
        args:
        width: width of rectangle
        height: height of rectangle"""

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
