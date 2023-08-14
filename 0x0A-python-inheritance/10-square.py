#!/usr/bin/python3
"""module contains BaseGeometry and subclass"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class to define a square"""
    def __init__(self, size):
        """instance of a square"""
        self.integer_validation("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """returns the area of the square"""
        return self.__size ** 2
