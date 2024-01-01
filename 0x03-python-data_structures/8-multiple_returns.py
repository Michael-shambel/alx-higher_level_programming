#!/usr/bin/python3
def multiple_returns(sentence):
    length_str = len(sentence)
    if length_str == 0:
        return 0, None
    else:
        return length_str, sentence[0]
