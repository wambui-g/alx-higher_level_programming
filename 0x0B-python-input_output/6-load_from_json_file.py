#!/usr/bin/python3
"""module that defines load_from_json_file function"""
import json


def load_from_json_file(filename):
    """function that creates an object from a json file"""
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
