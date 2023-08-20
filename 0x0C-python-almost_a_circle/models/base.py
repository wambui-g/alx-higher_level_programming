#!/usr/bin/python3
"""module to define Base class"""


class Base:
    """base class definition"""
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor that sets id to none"""
        if id is  not None:
            self.id = id
        else:
            Base.__nd_objects += 1
            self.id = Base.__nb_objects
