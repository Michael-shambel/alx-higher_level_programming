#!/usr/bin/python3
import sys
if __name__ == "__main__":
    arg_num = len(sys.argv)
    total = 0

    if (arg_num == 1):
        print("{}".format(0))
    else:
        for i in range(1, arg_num):
            total += int(sys.argv[i])
        print("{}".format(total))
