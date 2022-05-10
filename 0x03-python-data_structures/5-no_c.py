#!/usr/bin/python3
def no_c(my_string):
    string_without_C = ""
    for char in my_string:
        if char != 'c' and char != 'C':
            string_without_C += char
    return string_without_C
