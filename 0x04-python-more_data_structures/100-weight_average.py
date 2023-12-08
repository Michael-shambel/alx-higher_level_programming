#!/usr/bin/python3
def weight_average(my_list=[]):
    if (len(my_list) == 0):
        return 0
    T_P = 0
    T_W = 0

    for tup in my_list:
        T_P = T_P + tup[0] + tup[1]
        T_W = T_W + tup[1]
    return T_P / T_W
