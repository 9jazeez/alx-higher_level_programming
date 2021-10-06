#!/usr/bin/python3


"""A function that takes in two values
One must be a list of lists and the other
an integer or a float.
It returns a new matrix with divided elements

"""


def matrix_divided(matrix, div):
    """Matrix_division function

    Args:
    list (matrix): a list of lists
    int/float (div): an integer or a float

    Return: New list of lists(matrix) with divided
    elements.
    """

    try:
        row = []
        rowcopy = []
        column = []

        if not isinstance(matrix, list):
            raise TypeError('matrix must be a matrix\
                            (list of lists) of integers/floats')
        for i in matrix:
            if len(i) != len(matrix[0]):
                raise TypeError('Each row of the matrix\
                                    must have the same size')
            if not isinstance(i, list):
                raise TypeError('matrix must be a matrix\
                                (list of lists) of integers/floats')
            for a in i:
                if not isinstance(a, int) and not isinstance(a, float):
                    raise TypeError('matrix must be a matrix\
                                    (list of lists) of integers/floats')
                elif not isinstance(div, int) and not isinstance(div, float):
                    raise TypeError('div must be a number')
                elif div == 0:
                    raise ZeroDivisionError('division by zero')
                result = round(a / div, 2)
                row.append(result)
            rowCopy = row[0:]
            column.append(rowCopy)
            for m in range(len(row)):
                row.pop()
        return (column)
    except Exception as err:
        print(err)
