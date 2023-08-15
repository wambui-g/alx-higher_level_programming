#!/usr/bin/python3
"""module that defines read_file function"""


def read_file(filename=""):
    """function that reads from file and prints tostdout"""
    with open(filename, 'r', encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end='')
