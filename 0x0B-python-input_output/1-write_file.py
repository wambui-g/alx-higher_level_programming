#!/usr/bin/python3
"""module to define write_file function"""


def write_file(filename="", text=""):
    """function that writes a string to a txt file
    and returns no of charactes written"""
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
