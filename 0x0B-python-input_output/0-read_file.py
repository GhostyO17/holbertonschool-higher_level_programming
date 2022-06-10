#!/usr/bin/python3
"""
Opens and read a file
"""


def read_file(filename=""):
    """
    read_file: read a file passed as parameter
    """

    with open(filename, encoding='utf-8') as f:
        for line in f:
            print(line, end='')
