#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    my_dic = {}

    for key, value in a_dictionary.items():
        my_dic[key] = value * 2
    return my_dic
