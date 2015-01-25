from linhomy.issue26 import iter_contribute
from linhomy.issue27 import g_from_CD_matrix

def lists_from_matrix(matrix):

    return [
        list(map(int, row))
        for row in matrix
    ]


lists_from_matrix(g_from_CD_matrix(4)) == [
    [1, 0, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 1, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 1],
]
