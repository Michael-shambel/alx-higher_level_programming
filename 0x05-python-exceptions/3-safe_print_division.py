#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        solution = a / b
    except ZeroDivisionError:
        solution = None
    finally:
        print("Inside result: {}".format(solution))
        return solution
