#!/usr/bin/python3
"""
A function to rotate a 2D matrix
"""


def rotate_2d_matrix(matrix):
    """
    A function to rotate a 2D matrix
    """
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for row in matrix:
        row.reverse()
