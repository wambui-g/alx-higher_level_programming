#!/usr/bin/python3
"""module to define BaseGeometry"""


class BaseGeometry:
    """Class with public instance"""
    def area(self):
        """raises an exception when called"""
        raise Exception("area() is not implemented")
