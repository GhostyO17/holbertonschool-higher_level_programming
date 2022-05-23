#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        if isinstance(value, int):
            print("{:d}".format(value))
            return True
    except (TypeError, ValueError):
        return False
