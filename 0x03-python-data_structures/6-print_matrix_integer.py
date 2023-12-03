#!/usr?bin?python3
def print_matrix_integer(matrix=[[]]):
    for each_row in matrix:
        for each_col in each_row:
            if each_col != each_row[-1]:
                print("{:d}".format(each_col), end=" ")
            else:
                print("{:d}".format(each_col), end="")
        print()
