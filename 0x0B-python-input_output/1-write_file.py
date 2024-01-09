#!/usr/bin/python3
"""unction that writes ai string to a text
file and returns the number of characters written"""


def write_file(filename="", text=""):
    """writes a string to a text file and returns the number of characters
    args:
    filename: name of a file
    text: text that printed and counted
    return:
    a text file and number of characted in the file
    """
    with open(filename, 'w', encoding='UTF8') as f:
        number_of_char = f.write(text)
    return number_of_char
