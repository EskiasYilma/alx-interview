#!/usr/bin/python3
"""
A function that returns pascals triangle
"""


def pascal_triangle(n):
    """
    A function that returns pascals triangle
    """
    if n <= 0:
        return []

    t = []
    for row in range(n):
        if row == 0:
            t.append([1])
        else:
            prev_row = t[row - 1]
            new_row = [1]
            for i in range(1, len(prev_row)):
                new_row.append(prev_row[i - 1] + prev_row[i])
            new_row.append(1)
            t.append(new_row)

    return t
