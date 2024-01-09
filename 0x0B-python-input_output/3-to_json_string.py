#!/usr/bin/python3
"""function that returns the JSON
representation of an object (string)
"""
import json


def to_json_string(my_obj):
    """
    this function return the JSON representation
    arg: my_obj: obj converted to json
    return:
    str: json representation of string
    """
    return json.dumps(my_obj)
