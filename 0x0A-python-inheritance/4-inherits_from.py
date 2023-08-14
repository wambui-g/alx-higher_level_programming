#!/usr/bin/python3
"""module to define inherits function"""


def inherits_from(obj, a_class):
    """function that checks if obj is an instance of a class
    that inherited from the specified class a_class"""
    return(issubclass(type(obj), a_class) and type(obj) != a_class)
