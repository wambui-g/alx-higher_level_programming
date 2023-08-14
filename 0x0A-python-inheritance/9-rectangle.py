#!/usr/bin/python3
"""module contains BaseGeometry and Rectange"""


class BaseGeometry:
    """class with public instance and integer_validator"""
    def area(self):
        """raises exception when called"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """checks if value is > 0"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0;
        raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """representation of a rectangle"""
    def __init__(self, width, height):
        """instance of rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """returns area of defined rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """string rep of rectangle"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
