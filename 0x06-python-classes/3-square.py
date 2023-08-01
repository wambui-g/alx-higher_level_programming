#!/usr/bin/python3
"""Defines a Square class"""


class Square:
    """Square classinstance
    Attributes:
        __size (int): size of length
    """
    def __init__(self, size=0):
        """initializes the square
        Args:
            size (int): size of length
        Returns:
            None
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size

    def area(self):
        """gets the area of square
        Returns:
            area
        """
        return (self.__size) ** 2
