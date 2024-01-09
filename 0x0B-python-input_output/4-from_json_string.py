#!/usr/bin/python3

"""
function that returns an object
(Python data structure) represented by a JSON string
"""

import json


def from_json_string(my_str):
    """ this function returns an object repreented by JSON
    args:
    my_str: string
    return:
    object of json"""
    return json.loads(my_str)
