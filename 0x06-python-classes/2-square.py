#!/usr/bin/python3
"""defines a Square class"""


class Square:
    """Square class
    Attributes:
    __size (int): length
    """
    def __init__(self, size = 0)
    """Initializes the class
    Args:
    size (int): length
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
