#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix:
        squared_matrix = []
        for i in matrix:
            squared_matrix.append(list(map(lambda x: x * x, i)))
        return squared_matrix
