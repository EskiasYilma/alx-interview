#!/usr/bin/python3
"""
A script that reads stdin line by line and computes metrics:
"""
import fileinput


def print_status(status_dict, file_size):
    """
    Prints formatted file_size and status count
    """
    print("File size: {:d}".format(file_size))
    for i in sorted(status_dict.keys()):
        if status_dict[i] != 0:
            print("{}: {}".format(i, status_dict[i]))


status_dict = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0,
               "404": 0, "405": 0, "500": 0}
counter = 0
file_size = 0

try:
    for line in fileinput.input():
        if counter != 0 and counter % 10 == 0:
            print_status(status_dict, file_size)

        try:
            file_size += int(line.split(" ")[-1])
        except Exception:
            pass
        try:
            parsed = line.split(" ")[-2]
            if parsed in status_dict:
                status_dict[parsed] += 1
        except Exception:
            pass
        counter += 1
    print_status(status_dict, file_size)
except KeyboardInterrupt:
    print_status(status_dict, file_size)
    raise
