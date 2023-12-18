#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    num_printed = 0
    for i in range(x):
        try:
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                num_printed += 1
        except ValueError:
            pass
    print()
    return num_printed
