#!/usr/bin/python3
"""
A method that determines if a given data set represents a valid UTF-8 encoding
"""


def validUTF8(data):
    """
    A method that determines if a given data set represents a valid UTF-8 encoding
    """
    i = 0
    while i < len(data):
        b1 = data[i]
        b2 = data[i + 1] if i + 1 < len(data) else 0
        b3 = data[i + 2] if i + 2 < len(data) else 0
        b4 = data[i + 3] if i + 3 < len(data) else 0
        u1 = 0b0
        u2 = 0b110
        u3 = 0b1110
        u4 = 0b11110
        u = 0b10

        if b1 >> 7 == u1:
            i += 1
        elif b1 >> 5 == u2 and b2 >> 6 == u:
            i += 2
        elif b1 >> 4 == u3 and b2 >> 6 == u and b3 >> 6 == u:
            i += 3
        elif b1 >> 3 == u4 and b2 >> 6 == u and b3 >> 6 == u and b4 >> 6 == u:
            i += 4
        else:
            return False
    return True
