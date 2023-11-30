#!/usr/bin/python3
import sys
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    num_arg = len(sys.argv) - 1

    if num_arg != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a = sys.argv[1]
    sign = sys.argv[2]
    b = sys.argv[3]
    if sign not in ['+', '-', '*', '/']:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    a = int(a)
    b = int(b)

    if sign == '+':
        answer = add(a, b)
    elif sign == '-':
        answer = sub(a, b)
    elif sign == '*':
        answer = mul(a, b)
    else:
        answer = div(a, b)
    print("{} {} {} = {}".format(a, sign, b, answer))
