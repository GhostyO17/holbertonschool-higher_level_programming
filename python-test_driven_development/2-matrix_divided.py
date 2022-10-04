#!/usr/bin/python3
""" Function that divides all elements of a matrix """


def matrix_divided(matrix, div):
    """
    Takes a matrix as parameter and divides each element
    raises type error if wrong type of parameter is entered
    raises ZeroDivisionError when trying to divide by zero
    """

    if not type(div) in (float, int):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not type(matrix) is (list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) \
        of integers/floats")
    for array in matrix:
        if not type(array) is (list):
            raise TypeError("matrix must be a matrix (list of lists) \
            of integers/floats")
        if len(matrix[0]) is not len(array):
            raise TypeError("Each row of the matrix must have the same size")
        for new in array:
            if not type(new) in (float, int):
                raise TypeError("matrix must be a matrix (list of lists) \
                of integers/floats")
    return[[round(new / div, 2) for new in i] for i in matrix]
