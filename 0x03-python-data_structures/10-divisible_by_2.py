#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    multiple_2 = []

    for i in my_list:
        multiple_2.append(i % 2 == 0)
    return multiple_2
