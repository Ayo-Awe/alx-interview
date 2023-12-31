#!/usr/bin/python3

""" This module contains a python implementation
of the pascal triangle function
"""


def pascal_triangle(n):
    """pascal triangle function
    """
    if n <= 0:
        return []

    prev = pascal_triangle(n-1)

    return prev + [derive_next_row(get_item(prev, -1))]


def derive_next_row(previous_row):
    """derives the next row in the pascal triangle
    sequence given the previous row
    """
    if (previous_row is None):
        return [1]

    if (previous_row == [1]):
        return [1, 1]

    new_row = [1]

    for i, elm in enumerate(previous_row):

        # if not last row
        if (i != len(previous_row)-1):
            new_row.append(elm + previous_row[i+1])

    new_row.append(1)

    return new_row


def get_item(array, idx):
    """gets an item in an array
    without throwing an exception if
    the index is out of bounds
    """
    try:
        return array[idx]
    except IndexError:
        return None
