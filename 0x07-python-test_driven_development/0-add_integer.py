#!/usr/bin/python3
"""define the addition of integer"""


def add_integer(a, b=98):
    """
    Addition of two integers with the value of integer or float.

    :param a: First parameter
    :type a: int or float
    :param b: Second parameter (default is 98)
    :type b: int or float
    :return: The sum of two int or float
    :rtype: int
    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")


    return (int(a) + int(b))
