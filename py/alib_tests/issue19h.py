import numpy

from linhomy.cdrules import g_from_CD_factory

from linhomy.issue16 import c_rule
from linhomy.issue16 import d_rule

from linhomy.matrices import G_matrices

g_matrices = G_matrices(g_from_CD_factory(c_rule, d_rule))
P_from_h = g_matrices.P_from_h


def lists_from_cube(matrix):

    return [
        list(map(int, row))
        for tmp in matrix
        for row in tmp
    ]

## Dimension 5.

# Always P_from_h[0, n] is identiy matrix.
lists_from_cube(P_from_h[0, 5]) == [
    [1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 1],
]


# P_from_h[1, 4] is almost a zero-one matrix.
lists_from_cube(P_from_h[1, 4]) == [
    [1, 0, 0, 0, 0, 1, 0, 0],
    [0, 1, 1, 0, 0, 0, 2, 0],
    [0, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 1],
]

# P_from_h[2, 3] is a zero-one matrix.
lists_from_cube(P_from_h[2, 3]) == [
    [1, 0, 0, 0, 0, 0, 0, 1],
    [0, 1, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 1],
]

# P_from_g[3, 2] is rearrangement of P_from_g[2, 3] etc.


# Dimension 6.

# We skip P_from_g[0, 6] as it's the identity matrix.

# Here almost all zero-one.
lists_from_cube(P_from_h[1, 5]) == [
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0],
    [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
    [0, 0, -1, 0, 0, 0, 0, 0, 0, 1, -1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2],
]

# Here almost all zero-one.
lists_from_cube(P_from_h[3, 3]) == [
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
    [0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
    [0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 2, 0, 0, 1, 2, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2],
]


# Code to pick out the non zero-one entries.
def doit(n):

    zero_one = set([0, 1])
    value = []
    for m in range(n + 1):
        ell = n - m
        if  m > ell:
            continue
        matrix = P_from_h[m, ell]
        # TODO: provide an 'enumerate' for numpy matrices.
        i_lim, j_lim, k_lim = matrix.shape
        for i in range(i_lim):
            for j in range(j_lim):
                for k in range(k_lim):
                    c = matrix[i, j, k]
                    if c not in zero_one:
                        value.append((m, ell, i, j, k, c))

    return value


# The non zero-one entries for n = 6 (as from above).
doit(6) == [
    (1, 5, 0, 2, 10, 2),
    (1, 5, 0, 6, 2, -1),
    (1, 5, 0, 6, 10, -1),
    (1, 5, 0, 7, 12, 2),
    (2, 4, 0, 3, 12, 2),
    (3, 3, 0, 0, 12, 2),
    (3, 3, 1, 1, 2, 2),
    (3, 3, 1, 1, 6, 2),
    (3, 3, 2, 2, 12, 2),
]

# The non zero-one entries for n = 7.
doit(7) == [
    (1, 6, 0, 1, 15, -1),
    (1, 6, 0, 2, 16, -1),
    (1, 6, 0, 3, 16, 2),
    (1, 6, 0, 4, 17, 2),
    (1, 6, 0, 6, 15, -1),
    (1, 6, 0, 9, 19, 2),
    (2, 5, 0, 1, 15, 2),
    (2, 5, 0, 1, 19, 2),
    (2, 5, 0, 6, 2, -1),
    (2, 5, 0, 6, 15, -1),
    (3, 4, 1, 1, 2, 2),
    (3, 4, 1, 1, 6, 2),
    (3, 4, 1, 1, 10, -2),
    (3, 4, 1, 2, 10, 2),
    (3, 4, 1, 2, 16, -2),
    (3, 4, 2, 1, 19, 2),
]

# For n = 8, 9, 10 just count how many entries.
len(doit(8)) == 70
len(doit(9)) == 169
len(doit(10)) == 663
