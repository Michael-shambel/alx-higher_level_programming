#!/usr/bin/python3
""" function that return dictionary with simple data structure"""

def class_to_json(obj):
    """return a dictionary og an object"""
    return obj.__dict__
