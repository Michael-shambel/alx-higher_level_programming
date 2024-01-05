#!/usr/bin/python3
"""calculate area and perimeter of rectangle"""


class Rectangle:
    """clalculate the perimeter and area of the retangle"""
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        perim = 2 * (self.__width + self.__height)
        if self.__width == 0 or self.__height == 0:
            perim = 0
        return perim

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        str_rec = ""
        for i in range(self.__height):
            for j in range(self.__width):
                str_rec += '#'
            if i != self.__height - 1:
                str_rec += '\n' 
        return str_rec
