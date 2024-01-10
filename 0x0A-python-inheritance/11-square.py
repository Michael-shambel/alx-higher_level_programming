#!/usr/bin/python3
"""define rectangle subclass square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """represent a square"""
    def __init__(self, size):
        """initialize a square
        args:
        size: size of square
        """
        self.__size = 0
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
