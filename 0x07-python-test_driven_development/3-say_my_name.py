#!/usr/bin/python3
"""function that print first name and last name """


def say_my_name(first_name, last_name=""):
    """
    print the given full name
    the function take two argument
    the first argument is first name
    the secind argument is last name
    if the argumentonly have one argument return that argument

    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    if last_name:
        print(f"My name is {first_name} {last_name}")
    else:
        print(f"My name is {first_name}")
