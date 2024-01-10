#!/usr/bin/python3
""" this function inherit list class """


class MyList(list):
    """ print sorted list """

    def print_sorted(self):
        """ sort the agrgs"""
        print(sorted(self))
