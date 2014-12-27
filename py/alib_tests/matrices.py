from linhomy.matrices import F_from_IC

def lists_from_matrix(matrix):

    return [
        list(map(int, row))
        for row in matrix
    ]

lists_from_matrix(F_from_IC[4]) == [
    [1, 5, 10, 10, 30],
    [1, 6, 13, 13, 40],
    [1, 7, 15, 14, 45],
    [1, 8, 16, 14, 48],
    [1, 10, 21, 18, 64],
]
