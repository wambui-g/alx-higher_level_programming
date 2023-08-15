#!/usr/bin/python3
"""module to define append_write function"""


def append_write(filename="", text=""):
    """function that appends a string at the end of a txt file"""
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
