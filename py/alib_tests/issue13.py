from linhomy.issue13 import F_from_IC
from linhomy.issue13 import J_from_IC

def lists_from_matrix(matrix):

    return [
        list(map(int, row))
        for row in matrix
    ]

def lists_from_cube(matrix):

    return [
        list(map(int, row))
        for tmp in matrix
        for row in tmp
    ]


lists_from_matrix(F_from_IC[0]) == [
    [1],
]

lists_from_matrix(F_from_IC[1]) == [
    [1],
]

lists_from_matrix(F_from_IC[2]) == [
    [1, 1],
    [3, 4],
]

lists_from_matrix(F_from_IC[3]) == [
    [1, 1, 1],
    [4, 5, 6],
    [6, 8, 9],
]


sorted(J_from_IC) == [
    (0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9),
    (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8),
    (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7),
    (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6),
    (4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5),
    (5, 0), (5, 1), (5, 2), (5, 3), (5, 4),
    (6, 0), (6, 1), (6, 2), (6, 3),
    (7, 0), (7, 1), (7, 2),
    (8, 0), (8, 1),
    (9, 0),
]

# Correct.
lists_from_cube(J_from_IC[0, 0]) == [
    [1],
]

# C operator - correct.
lists_from_cube(J_from_IC[0, 1]) == [
    [1, 0],
]

# C operator - correct.
lists_from_cube(J_from_IC[0, 2]) == [
    [1, 0, 0],
    [0, 1, 0],
]

lists_from_cube(J_from_IC[2, 2]) == [
    [1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, -1, 2, -1],
]

lists_from_cube(J_from_IC[2, 3]) == [
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, -1, 2, -1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, -1, 1, 1, -1, 0],
]
