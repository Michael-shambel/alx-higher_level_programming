#!/usr/bin/python3
"""this class about creating a square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """this class is about a square class"""

    def __init__ (self, size, x=0, y=0, id=None):
        """this is the constranctor of a square inherited from
        Rectangle class and it is going to take the attributes
        of rectangle"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """this print the attributes"""
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}")
