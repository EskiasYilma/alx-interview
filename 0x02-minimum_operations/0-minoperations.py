#!/usr/bin/python3
"""
In a text file, there is a single character H. Your text editor can
execute only two operations in this file: Copy All and Paste. Given
a number n, write a method that calculates the fewest number of
operations needed to result in exactly n H characters in the file.

Prototype: def minOperations(n)
Returns an integer
If n is impossible to achieve, return 0
"""


def minOperations(n):
    """
    Returns an integer
    If n is impossible to achieve, return 0
    """

    if n == 1:
        return 0

    minOper = [0] * (n + 1)

    for i in range(2, n + 1):
        minOper[i] = i
        for j in range(2, i // 2 + 1):
            if i % j == 0:
                minOper[i] = min(minOper[i], minOper[j] + i // j)

    return minOper[n]
