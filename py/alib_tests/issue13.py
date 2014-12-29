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

# C operator - wrong.
lists_from_cube(J_from_IC[0, 1]) == [
    [-5, 2],
]

# C operator - wrong.
lists_from_cube(J_from_IC[0, 2]) == [
    [-9, 1, 1],
    [-13, 2, 1],
]

lists_from_cube(J_from_IC[2, 2]) == [
    [250, 6, -53, -54, 27, 0, -32, 21],
    [344, 2, -67, -77, 37, 2, -43, 28],
    [344, 2, -67, -77, 37, 2, -43, 28],
    [474, -8, -82, -109, 50, 5, -57, 37],
]

lists_from_cube(J_from_IC[2, 3]) == [
    [-6404, 3114, -1318, 2710, -752, -1231, 342, -42, 1965, -779, 236, -479, 146],
    [-8686, 4221, -1800, 3675, -1014, -1677, 466, -59, 2665, -1055, 323, -647, 196],
    [-9869, 4811, -2058, 4180, -1151, -1918, 527, -64, 3026, -1194, 363, -731, 222],
    [-8686, 4221, -1800, 3675, -1014, -1677, 466, -59, 2665, -1055, 323, -647, 196],
    [-11787, 5723, -2459, 4987, -1368, -2287, 637, -84, 3616, -1430, 443, -874, 263],
    [-13397, 6526, -2816, 5675, -1552, -2616, 719, -91, 4107, -1618, 498, -988, 298],
]
