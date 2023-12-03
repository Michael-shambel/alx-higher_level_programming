#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    fir_tuple = tuple_a + (0, 0)
    sec_tuple = tuple_b + (0, 0)
    total = (fir_tuple[0] + sec_tuple[0], fir_tuple[1] + sec_tuple[1])
    return total
