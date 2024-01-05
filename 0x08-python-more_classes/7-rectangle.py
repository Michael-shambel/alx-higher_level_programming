#!/usr/bin/python3
"""calculate area and perimeter of rectangle"""


class Rectangle:
    """clalculate the perimeter and area of the retangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        type(self).number_of_instances += 1
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
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((2 * self.__width) + (2 * self.__height))

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        str_rec = []
        for i in range(self.__height):
            for j in range(self.__width):
                str_rec.append(str(self.print_symbol))
            if i != self.__height - 1:
                str_rec.append("\n")
        return ("".join(str_rec))

    def __repr__(self):
        return "{}({}, {})".format(
                type(self).__name__, self.__width, self.__height)

    def __del__(self):
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
