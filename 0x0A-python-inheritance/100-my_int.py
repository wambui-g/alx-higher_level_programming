#!/usr/bin/python3
"""module that defines MyInt"""


class MyInt(int):
    """MyInt class for opposites"""
    def __new__(cls, *args, **kwargs):
        """new class instance"""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """what was != is =="""
        return int(self) != other

    def __ne__(self, other):
        """what was == is !="""
        return int(self) == other
