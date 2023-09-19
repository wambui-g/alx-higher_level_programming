#!/usr/bin/python3
"""Module to define square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """definition of subclass square"""

    def __init__(self, size, x=0, y=0, id=None):
        """constructor to create class instance"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getter method for size"""
        return self.width

    @size.setter
    def size(self, value):
        """setter for size"""
        if type(value) != int:
            return TypeError("width must be an integer")
        if value <= 0:
            return ValueError("width must be > 0")

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """function to assign values"""
        if len(args) == 0:
            for key, val in kwargs.items():
                self.__setattr__(key, val)
            return

        try:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]
        except IndexError:
            pass

    def __str__(self):
        """string format of sqaure"""
        return "[{}] ({}) {}/{} - {}".format(type(self).__name__,
                                             self.id, self.x, self.y,
                                             self.width)

    def to_dictionary(self):
        """dictionary rep of square"""
        return {'id': getattr(self, "id"),
                'size': getattr(self, "width"),
                'x': getattr(self, "x"),
                'y': getattr(self, "y")}
