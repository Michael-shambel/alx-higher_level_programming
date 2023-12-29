#!/usr/bin/python3
import sys
if __name__ == "__main__":
    arg_num = len(sys.argv) - 1

    if arg_num == 0:
        print("0 arguments.")
    elif arg_num == 1:
        print("{} argument:".format(arg_num))
        print("{}: {}".format(arg_num, sys.argv[arg_num]))
    else:
        print("{} arguments:".format(arg_num))
        for i in range(1, arg_num + 1):
            print("{}: {}".format(i, sys.argv[i]))
