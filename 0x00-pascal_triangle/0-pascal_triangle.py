#!/usr/bin/python3
"""
A function that returns pascals triangle
"""

from math import factorial


def pascal_triangle(n):
    """
    A function that returns pascals triangle
    """
    if n <= 0:
        return []
    for i in range(n):
        print("[", end="")
        for j in range(i+1):
            print(factorial(i)//(factorial(j)*factorial(i-j)),
                  end="," if j < i else "")
        print(']')
