#!/usr/bin/python3

""" function that returns a dictionary with a simple data structure"""


def class_to_json(obj):
    """return a dictionary of an object"""
    return obj.__dict__
