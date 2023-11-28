#!/usr/bin/python3
def uppercase(str):
    newcap = ""
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            i = chr(ord(i) - 32)
            newcap = newcap + i
        else:
            newcap = newcap + i
    print("{}".format(newcap))
