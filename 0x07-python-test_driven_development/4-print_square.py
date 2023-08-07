#!/usr/bin/python3
"""module that defines 4-print_square"""


def print_square(size):
    """prints a square of length size with #"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")
    if size > 0:
        print(("#" * size + "\n") * size, end="")
