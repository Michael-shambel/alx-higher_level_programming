#!/usr/bin/python3
""" this function print the square of sign # """


def print_square(size):
    """ 
    this function take a size of an integer 
    the function have one argument called size
    it take tehe argument and print sign of # hashtag
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for _ in range(size):
        print("#" * size)
