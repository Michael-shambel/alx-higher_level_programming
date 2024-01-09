#!/usr/bin/python3
""" this function will use for read file"""


def read_file(filename=""):
    """ this object read a text file and print its content to stdout"""
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end='')
