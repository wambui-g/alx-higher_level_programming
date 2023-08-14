#!/usr/bin/python3
"""module to define is_same_class function"""


def is_same_class(obj, a_class):
    """"function that checks whether obj is in a_class"""
    return (type(obj) == a_class)
