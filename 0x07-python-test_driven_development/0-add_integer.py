#!/usr/bin/python3
"""
adds integer a and b
"""


def add_integer(a, b=98):
    """Return the sum of a and b"""
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer or float")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer or float")

    a = int(a)
    b = int(b)

    return a + b
