import numpy
from linhomy.bilinear import J_from_CD
from linhomy.matrices import _cache
from linhomy.matrices import CD_from_F

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

lists_from_cube(J_from_CD[2, 2]) == [
    [0, 0, 0, 0, 0, 0, 2, -1],
    [0, -1, 0, 0, 0, 0, -2, 1],
    [0, -1, 0, 0, 0, 0, -2, 1],
    [1, 2, 0, 0, 0, 0, 2, -1],
]

# Shows previous calculation is wrong.
list(numpy.dot(CD_from_F[5], _cache[b'J(CC,CC)'])) == [1, 0, 0, 0, 0, 0, 0, 0]

# Shows previous calculation is wrong.
list(
    + numpy.dot(CD_from_F[5], _cache[b'J(IC,CC)'])
    - numpy.dot(CD_from_F[5], _cache[b'J(CC,CC)'])
) == [0, 1, 0, 0, 0, 0, 0, 0]

# Shows previous calculation is wrong.
list(
    + numpy.dot(CD_from_F[5], _cache[b'J(IC,IC)'])
    - numpy.dot(CD_from_F[5], _cache[b'J(IC,CC)'])
    - numpy.dot(CD_from_F[5], _cache[b'J(CC,IC)'])
    + numpy.dot(CD_from_F[5], _cache[b'J(CC,CC)'])
) == [0, 0, 0, 0, 0, 0, 2, -1]


lists_from_cube(J_from_CD[2, 3]) == [
    [0, 1, 0, 0, 0, 0, 2, -1, 0, 1, 1, -1, 0],
    [0, -1, 0, 0, 0, 0, -2, 1, 0, 0, 0, 0, 0],
    [0, -1, 0, 0, 0, 0, 0, 0, 0, -1, -1, 1, 0],
    [-1, -2, -1, 0, 0, 0, -2, 1, 0, -1, -1, 1, 0],
    [1, 2, 0, 0, 0, 0, 2, -1, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, -1, 0],
]
