#!/usr/bin/python3
"""text file insertion"""


def append_after(filename="", search_string="", new_string=""):
    """ insert text at the end
    args:
    filename: name of the file
    search_string: search string with in the file
    new_string: new string to be inserted
    """
    text_file = ""
    with open(filename, 'r') as f:
        for l in f:
            text_file += l
            if search_string in l:
                text_file += new_string
