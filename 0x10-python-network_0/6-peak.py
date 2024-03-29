#!/usr/bin/python3
"""Write a function that finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """find a peak value of list"""
    if not list_of_integers:
        return None
    left_side = 0
    right_side = len(list_of_integers) - 1

    while left_side < right_side:
        mid_side = (left_side + right_side) // 2
        if list_of_integers[mid_side] < list_of_integers[mid_side + 1]:
            left_side = mid_side + 1
        else:
            right_side = mid_side

    return list_of_integers[left_side]
