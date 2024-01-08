#!/usr/bin/python3
""" define a class is inherited """


def is_kind_of_class(obj, a_class):
    """ this function accept two argi=umenrtes and 
    check if the object is in a class """
    if isinstance(obj, a_class):
        return True
    return False
