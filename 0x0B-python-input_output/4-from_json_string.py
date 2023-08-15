#!/usr/bin/python3
"""module to define from_json_string function"""
import json


def from_json_string(my_str):
    """function that returns object represented by a json string"""
    return json.loads(my_str)
