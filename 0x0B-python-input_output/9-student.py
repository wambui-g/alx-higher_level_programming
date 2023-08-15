#!/usr/bin/python3
"""module to define student class"""


class Student:
    """class student instance"""

    def __init__(self, first_name, last_name, age):
        """initialize the class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """method that returns directory desc"""
        return self.__dict__.copy()
