#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in range(len(matrix)):
        a = []
        for j in range(len(matrix[i])):
            a.append(matrix[i][j] ** 2)
        new_matrix.append(a)
    return(new_matrix)
