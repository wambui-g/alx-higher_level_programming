#!/usr/bin/python3
"""module to define append_after"""


def append_after(filename="", search_string="", new_string=""):
    """function to append a new line when string is found"""
    resline = []
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            resline += [line]
            if line.find(search_string) != -1:
                resline += [new_string]

    with open(filename, 'w', encoding="utf-8") as f:
        f.write("".join(resline))
