#!/usr/bin/python3
"""module that defines the save_to_json_file function"""
import json


def save_to_json_file(my_obj, filename):
    """function that writes an object to text usig json rep"""
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
