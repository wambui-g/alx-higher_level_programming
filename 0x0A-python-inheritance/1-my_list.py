#!/usr/bin/python3
"""module defines MyList subclass that inherits from class"""


class MyList(list):
    """a subclass of list class"""
    def __init__(self):
        """initializes the object"""
        super().__init__()

    def print_sorted(self):
        """function to print in sorted format"""
        print(sorted(self))
