#!/usr/bin/python3
def no_c(my_string):
    new_strr = ''
    for i in my_string:
        if i != 'c' and i != 'C':
            new_strr += i
    return new_strr
