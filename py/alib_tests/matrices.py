import numpy

from linhomy.cdrules import g_from_CD_helper

from linhomy.constants import FIBWORDS
from linhomy.matrices import _cache
from linhomy.matrices import F_from_IC
from linhomy.matrices import IC_from_F

from linhomy.matrices import G_matrices

MAX = 6
g_matrices = G_matrices(g_from_CD_helper, max=MAX)

g_from_F = g_matrices.g_from_F


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
    [1, 1, 1, 1, 1],
    [5, 6, 7, 8, 10],
    [10, 13, 15, 16, 21],
    [10, 13, 14, 14, 18],
    [30, 40, 45, 48, 64],
]

lists_from_matrix(IC_from_F[4]) == [
    [16, -5, 2, -4, 1],
    [-10, 4, -4, 3, 0],
    [0, -2, 4, 0, -1],
    [-15, 7, -3, 4, -1],
    [10, -4, 1, -3, 1],
]


from linhomy.matrices import h_from_g
h_from_g[2] = [
    # Rows into columns.
    [1, 0],                     # h_0 = g_0
    [1, 1],                     # h_1 = g_0 + g_1
]

h_from_g[3] = [
    [1, 0, 0],                  # h_0 = g_0
    [0, 1, 0],                  # h_{:} = g_{:}
    [1, 0, 1],                  # h_1 = g_0 + g_1
]

h_from_g[4] = [
    [1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [1, 0, 0, 1, 0],
    [1, 0, 0, 1, 1],            # h_2 = g_0 + g_1 + g_2
]

h_from_g[5] = [
    [1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [1, 0, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 1, 0, 1],   # h_2 = g_0 + g_1 + g_2
]


g_from_CD = g_matrices.g_from_CD
CD_from_g = g_matrices.CD_from_g

lists_from_matrix(g_from_CD[2]) == [
    [1, 0],
    [0, 1],
]

lists_from_matrix(g_from_CD[3]) == [
    [1, 0, 0],
    [0, 1, 0],
    [0, 1, 1],
]

from linhomy.matrices import CD_from_IC_helper

list(CD_from_IC_helper(b'')) == [
    b'',
]

list(CD_from_IC_helper(b'\x01')) == [
    b'\x01',
]

list(CD_from_IC_helper(b'\x02')) == [
    b'\x01\x01',
    b'\x02',
]

list(CD_from_IC_helper(b'\x02\x01\x02\x02')) == [
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

# IC = D + CC.
lists_from_matrix(CD_from_IC[2]) == [
    [1, 1],
    [0, 1],
]

# Here's how things are labelled.
FIBWORDS[2] == (b'\x01\x01', b'\x02')
list(numpy.dot(CD_from_IC[2], [1, 0])) == [1, 0]
list(numpy.dot(CD_from_IC[2], [0, 1])) == [1, 1]

lists_from_matrix(CD_from_IC[3]) == [
    [1, 1, 1],
    [0, 1, 0],
    [0, 0, 1],
]

lists_from_matrix(CD_from_IC[4]) == [
    [1, 1, 1, 1, 1],
    [0, 1, 0, 0, 1],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 1],
    [0, 0, 0, 0, 1],
]

lists_from_matrix(IC_from_CD[4]) == [
    [1, -1, -1, -1, 1],
    [0, 1, 0, 0, -1],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, -1],
    [0, 0, 0, 0, 1],
]



lists_from_matrix(g_from_CD[4]) == [
    [1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 1],
]

lists_from_matrix(CD_from_g[4]) == [
    [1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, -1, 1, 0, 0],
    [0, 0, -1, 1, 0],
    [0, 0, 0, 0, 1],
]


from linhomy.matrices import J_from_IC
from linhomy.matrices import P_from_IC

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

sorted(
    (i, j)
    for (i, j) in P_from_IC
    if i + j == 10
) == [
    (0, 10), (1, 9), (2, 8), (3, 7), (4, 6), (5, 5),
    (6, 4), (7, 3), (8, 2), (9, 1), (10, 0),
]


lists_from_cube(P_from_IC[2, 2]) == [
    [1, -1, 0, 0, 1],
    [0, -1, 0, 1, 1],
    [0, -1, 0, 1, 1],
    [0, -2, 0, 1, 2],
]


lists_from_cube(J_from_IC[2, 2]) == [
    [1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, -1, 2, -1],
]


# Shows previous calculation is correct.
list(numpy.dot(IC_from_F[5], _cache[b'CCCCC'])) == [1, 0, 0, 0, 0, 0, 0, 0]
list(numpy.dot(IC_from_F[5], _cache[b'CCCIC'])) == [0, 1, 0, 0, 0, 0, 0, 0]
list(numpy.dot(IC_from_F[5], _cache[b'J(IC,IC)'])) == [0, 0, 1, 0, 0, -1, 2, -1]


lists_from_cube(J_from_IC[2, 3]) == [
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, -1, 2, -1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, -1, 1, 1, -1, 0],
]

len(lists_from_cube(J_from_IC[4, 5])) == 5 * 8


from linhomy.matrices import J_from_CD
from linhomy.matrices import CD_from_F

sorted(J_from_CD) == sorted(J_from_IC)

lists_from_cube(J_from_CD[2, 2]) == [
    [1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 2, -1],
]

# Shows previous calculation is correct.
list(numpy.dot(CD_from_F[5], _cache[b'J(CC,CC)'])) == [1, 0, 0, 0, 0, 0, 0, 0]

# Shows previous calculation is correct.
list(
    + numpy.dot(CD_from_F[5], _cache[b'J(IC,CC)'])
    - numpy.dot(CD_from_F[5], _cache[b'J(CC,CC)'])
) == [0, 1, 0, 0, 0, 0, 0, 0]

# Shows previous calculation is correct.
list(
    + numpy.dot(CD_from_F[5], _cache[b'J(IC,IC)'])
    - numpy.dot(CD_from_F[5], _cache[b'J(IC,CC)'])
    - numpy.dot(CD_from_F[5], _cache[b'J(CC,IC)'])
    + numpy.dot(CD_from_F[5], _cache[b'J(CC,CC)'])
) == [0, 0, 0, 0, 0, 0, 2, -1]


lists_from_cube(J_from_CD[2, 3]) == [

    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 2, -1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, -1, 0],
]


J_from_g = g_matrices.J_from_g

sorted(J_from_g) == sorted(
    (i, j)
    for i, j in J_from_IC
    if i + j < MAX
)

# This is correct.  It is the cone rule.
lists_from_cube(J_from_g[0, 0]) == [
    [1],
]

# This is correct.  It is the cone rule.
lists_from_cube(J_from_g[0, 1]) == [
    [1, 0],
]

# This is correct.  It is the cone rule.
lists_from_cube(J_from_g[0, 2]) == [
    [1, 0, 0],
    [0, 1, 1]
]


# Not obviously a wrong calcuation.
lists_from_cube(J_from_g[2, 2]) == [
    [1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 1, 0, 0],
    [0, 1, 1, 1, 0, 1, 0, 0],
    [0, 0, 2, 0, 0, 0, 2, 1],
]


# Check the above calculation.
g_from_F = g_matrices.g_from_F

# Agrees with above.
list(numpy.dot(g_from_F[5], _cache[b'CCCCC'])) == [1, 0, 0, 0, 0, 0, 0, 0]

# Agrees with above.
list(
    + numpy.dot(g_from_F[5], _cache[b'J(IC,CC)'])
    - numpy.dot(g_from_F[5], _cache[b'J(CC,CC)'])
) == [0, 1, 1, 1, 0, 1, 0, 0]

_cache[b'J(IC,CC)'] != _cache[b'CICCC']
_cache[b'J(IC,CC)'] == _cache[b'CCCIC']

# Agrees with above.
list(
    + numpy.dot(g_from_F[5], _cache[b'J(IC,IC)'])
    - numpy.dot(g_from_F[5], _cache[b'J(CC,IC)'])
    - numpy.dot(g_from_F[5], _cache[b'J(IC,CC)'])
    # TODO: Note that previously '*' for '+' did not raise exception.
    + numpy.dot(g_from_F[5], _cache[b'J(CC,CC)'])
) == [0, 0, 2, 0, 0, 0, 2, 1]


# Not obviously a wrong calculation.
lists_from_cube(J_from_g[2, 3]) == [
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 2, -2, 0, 1, 2, 1, 0, 1, -2, 0, 0],
    [0, 0, 0, 2, 0, 0, 0, 0, 0, 1, 2, 1, 0],
]
