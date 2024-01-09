#!/usr/bin/python3
"""
function that writes an Object to a text file
using a JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """
    this  module accept two argument and write into text file
    args:
    my_obj: object file
    filename: name of my file
    return:
    afile"""
    if isinstance(my_obj, list):
        my_obj = list(my_obj)
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
