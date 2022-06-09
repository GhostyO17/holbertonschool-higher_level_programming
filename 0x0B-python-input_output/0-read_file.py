#!/usr/bin/python3
"""
Opens and read a file
"""


def read_file(filename=""):
    """
    read_file: read a file pass as parameter
    """

    with open(filename) as f:
        f_read = f.read
        print(f_read, end='')
