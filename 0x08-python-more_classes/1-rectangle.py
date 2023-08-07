#!/usr/bin/python3
"""module to define a rectangle"""


class Rectangle:
    """defined an empty Rectangle class"""
    def __init__(self, width=0, height=0):
        """initializes the rectangle"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """getter for private instance attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for private instance attribute"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise TypeError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter forprivate instance"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for private instance"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value