#!/usr/bin/python3
def add_integer(a, b=98):
    """
    addition of two integers with the value of interger or float
    :param a: First parameter
    :type a: int or float
    :param b: second parameter
    :type b: int or float
    :return: the sum of two int or float
    :rtype: int
    """

    if a is None:
        raise TypeError("a must be an integer")
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")

    if isinstance(b, str):
        raise TypeError("b must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float")

    a = int(a)
    b = int(b)

    return a + b
