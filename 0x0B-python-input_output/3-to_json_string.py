#!/usr/bin/python3
import json
"""function that returns the JSON
representation of an object (string)
"""


def to_json_string(my_obj):
    """
    this function return the JSON representation
    arg: my_obj: obj converted to json
    return:
    str: json representation of string
    """
    return json.dumps(my_obj)
