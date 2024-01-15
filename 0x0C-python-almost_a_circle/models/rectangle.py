#!/usr/bin/python3
"""this is a class of rectangle with bse inheritance"""
from models.base import Base


class Rectangle(Base):
    """this is rectangle class with inheritance of Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """this is constractor method
        args:
            width: width of the rectangle
            height: height of the rectangle
            x: x cordinate of the rectangle
            y: y coredinate of the rectangle"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """this getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """this is setter for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """this is getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """this is setter for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """this is getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """this is setter for x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """this is getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """this is setter for y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """calculate the erea of rectangle"""
        return self.width * self.height

    def display(self):
        """display hashtag sigh"""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """print the string format"""
        return (
            f"[Rectangle] ({self.id}) {self.x}/{self.y} - "
            f"{self.width}/{self.height}"
            )

    def update(self, *args, **kwargs):
        """this is method for assign argument

        args:
            - id attribute
            - widrh attribute
            - height attribute
            - x cordinate attribute
            - y coordinate attribute"""
        attributes = ["id", "width", "height", "x", "y"]

        if args:
            for i, value in enumerate(args):
                if value is None:
                    initial_values = [
                            initial_value_for_id,
                            initial_value_for_width,
                            initial_value_for_height,
                            initial_value_for_x,
                            initial_value_for_y
                            ]
                    setattr(self, attributes[i], initial_values[i])
                else:
                    setattr(self, attributes[i], value)
        elif kwargs:
            for key, value in kwargs.items():
                if key in attributes:
                    if value is None:
                        initial_value = initial_value_for_key
                        setattr(self, key, initial_value)
                    else:
                        setattr(self, key, value)

    def to_dictionary(self):
        """return dictionary representation of a rectangle"""
        return {
                "id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y
                }
