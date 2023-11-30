#!/usr/bin/python3
import sys
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    num_arg = len(sys.argv) - 1

    if num_arg != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
