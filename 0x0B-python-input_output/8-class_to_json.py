#!/usr/bin/python3
"""module to define class_to_json function"""


def class_to_json(obj):
    """function that retunrs the dictionary description of an obj"""

    res = {}
    if hasattribute(obj, "__dict__"):
        res = obj.__dic__.copy()
    return res
