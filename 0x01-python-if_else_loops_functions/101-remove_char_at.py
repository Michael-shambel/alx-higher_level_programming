#!/usr/bin/python3
def remove_char_at(str, n):
    newstr = ""
    if n > len(str) or n < 0:
        return str
    else:
        for i in range(len(str)):
            if str[i] != str[n]:
                newstr += str[i]
    return newstr
