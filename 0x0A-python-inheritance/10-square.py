#!/usr/bin/python3
"""define rectangle with square subclass"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """represent square"""

    def __init__(self, size):
        """initialize a new square
        args:
        size: size of square"""
        self.__size = 0
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
