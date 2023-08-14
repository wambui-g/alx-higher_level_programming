#!/usr/bin/python3
"""module defines a function lookup"""


def lookup(obj):
    """function that returns list of all available attributes and methods"""
    return dir(obj)
