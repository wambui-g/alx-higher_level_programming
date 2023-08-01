#!/usr/bin/python3
"""accesses and updates private attribute"""


class Square:
    """Square class instant
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
        self.size = size

    def area(self):
        """returns area of square
        Returns:
            area of the square
        """
        return (self.__size) ** 2

    @property
    def size(self):
        """getter __size
        Returns:
            size of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """setter of __size
        Args:
            value (int): size of length
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
