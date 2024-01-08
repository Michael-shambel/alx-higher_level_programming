#!/usr/bin/python3
"""define the checking of inheritance"""


def inherits_from(obj, a_class):
    """ this function accept two argument which is
    object and a class so it check weather  if the object
    is an instance of a class that inherited
    (directly or indirectly) from the specified class """

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
