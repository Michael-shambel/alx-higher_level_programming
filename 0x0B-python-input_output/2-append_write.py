#!/usr/bin/python3
"""function that appends a string at the end of a text file
and returns the number of characters added"""


def append_write(filename="", text=""):
    """function that appends a string at the end of a text file
    and returns the number of characters added
    accept two args:
    filename: the filename of txt
    text: a text added to the file
    return:
    number of text added and file it self
    """
    with open(filename, 'a', encoding='UTF8') as f:
        num_new_char = f.write(text)
    return num_new_char
