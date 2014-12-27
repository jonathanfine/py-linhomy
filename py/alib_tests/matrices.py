from linhomy.matrices import F_from_IC
from linhomy.matrices import IC_from_F

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


lists_from_matrix(F_from_IC[4]) == [
    [1, 5, 10, 10, 30],
    [1, 6, 13, 13, 40],
    [1, 7, 15, 14, 45],
    [1, 8, 16, 14, 48],
    [1, 10, 21, 18, 64],
]

lists_from_matrix(IC_from_F[4]) == [
    [16, -10, 0, -15, 10],
    [-5, 4, -2, 7, -4],
    [2, -4, 4, -3, 1],
    [-4, 3, 0, 4, -3],
    [1, 0, -1, -1, 1],
]


from linhomy.matrices import IC_from_CD_helper

list(IC_from_CD_helper(b'')) == [
    b'',
]

list(IC_from_CD_helper(b'\x01')) == [
    b'\x01',
]

list(IC_from_CD_helper(b'\x02')) == [
    b'\x01\x01',
    b'\x02',
]

list(IC_from_CD_helper(b'\x02\x01\x02\x02')) == [
    b'\x01\x01\x01\x01\x01\x01\x01',
    b'\x01\x01\x01\x01\x01\x02',
    b'\x01\x01\x01\x02\x01\x01',
    b'\x01\x01\x01\x02\x02',
    b'\x02\x01\x01\x01\x01\x01',
    b'\x02\x01\x01\x01\x02',
    b'\x02\x01\x02\x01\x01',
    b'\x02\x01\x02\x02',
]


from linhomy.matrices import IC_from_CD
from linhomy.matrices import CD_from_IC

lists_from_matrix(IC_from_CD[4]) == [
    [1, 0, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [1, 0, 1, 0, 0],
    [1, 0, 0, 1, 0],
    [1, 1, 0, 1, 1],
]

lists_from_matrix(CD_from_IC[4]) == [
    [1, 0, 0, 0, 0],
    [-1, 1, 0, 0, 0],
    [-1, 0, 1, 0, 0],
    [-1, 0, 0, 1, 0],
    [1, -1, 0, -1, 1],
]


from linhomy.matrices import J_from_IC

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

lists_from_cube(J_from_IC[2, 2]) == [
    [1, 6, 15, 20, 60, 15, 60, 90],
    [1, 7, 19, 26, 79, 19, 79, 120],
    [1, 7, 19, 26, 79, 19, 79, 120],
    [1, 8, 24, 34, 104, 24, 104, 160],
]

lists_from_cube(J_from_IC[2, 3]) == [
    [1, 7, 21, 35, 105, 35, 140, 210, 21, 105, 210, 210, 630],
    [1, 8, 26, 45, 136, 45, 184, 278, 26, 136, 278, 278, 840],
    [1, 9, 30, 51, 156, 49, 207, 315, 27, 150, 312, 309, 945],
    [1, 8, 26, 45, 136, 45, 184, 278, 26, 136, 278, 278, 840],
    [1, 9, 32, 58, 176, 58, 242, 368, 32, 176, 368, 368, 1120],
    [1, 10, 37, 66, 202, 63, 272, 417, 33, 194, 413, 409, 1260],
]

len(lists_from_cube(J_from_IC[4, 5])) == 5 * 8
