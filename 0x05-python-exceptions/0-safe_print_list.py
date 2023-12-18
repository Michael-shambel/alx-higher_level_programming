#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    num_print = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            num_print += 1
    except IndexError:
        pass
    print()
    return num_print
