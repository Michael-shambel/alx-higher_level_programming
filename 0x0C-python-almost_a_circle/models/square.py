#!/usr/bin/python3
"""this class about creating a square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """this class is about a square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """this is the constranctor of a square inherited from
        Rectangle class and it is going to take the attributes
        of rectangle"""
        if id is None:
            super().__init__(size, size, x, y)
        else:
            super().__init__(size, size, x, y)

    def __str__(self):
        """this print the attributes"""
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}")

    @property
    def size(self):
        """this is getter for attribute"""
        return self.width

    @size.setter
    def size(self, value):
        """this is setter for attribute"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ update the square
        args:
        1st argument should be the id attribute
        2nd argument should be the size attribute
        3rd argument should be the x attribute
        4th argument should be the y attribute"""
        attributes = ["id", "size", "x", "y"]

        if args:
            for i in range(len(args)):
                setattr(self, attributes[i], args[i])
        elif kwargs and not args:
            for key, value in kwargs.items():
                if key in attributes:
                    setattr(self, key, value)

    def to_dictionary(self):
        """eturns the dictionary representation of a Square"""
        return {
                "id": self.id,
                "size": self.width,
                "x": self.x,
                "y": self.y
                }
