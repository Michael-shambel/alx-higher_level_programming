#!/usr?bin?python3
def print_matrix_integer(matrix=[[]]): 
    for _row_ in matrix:
        for x, val in enumerate(_row_):
            if x != len(_row_) - 1:
                print("{:d}".format(val), end=" ")
            else:
                print("{:d}".format(val))
