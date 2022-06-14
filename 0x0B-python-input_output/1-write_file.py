#!/usr/bin/python3
"""
Writes a string to a text file
"""


def write_file(filename="", text=""):
    """
    Args:
        filename: text file. Defaults to "".
        text: string to attach. Defaults to "".
    """
    with open(filename, 'w', encoding='utf-8') as rf:
        return rf.write(text)
