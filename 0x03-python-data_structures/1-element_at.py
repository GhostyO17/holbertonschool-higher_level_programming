#!/usr/bin/python3
from tokenize import maybe
from typing import List


def element_at(my_list, idx):
    if idx < 0 and idx > len(my_list):
        return None
    else:
        return my_list[idx]
