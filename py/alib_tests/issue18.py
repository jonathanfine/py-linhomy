import numpy

from linhomy.cdrules import g_from_CD_factory

from linhomy.issue16 import c_rule
from linhomy.issue16 import d_rule

from linhomy.matrices import G_matrices

g_matrices = G_matrices(g_from_CD_factory(c_rule, d_rule))
P_from_g = g_matrices.P_from_g


def lists_from_cube(matrix):

    return [
        list(map(int, row))
        for tmp in matrix
        for row in tmp
    ]

## Dimension 5.

# Always P_from_g[0, n] is identiy matrix.
lists_from_cube(P_from_g[0, 5]) == [
    [1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 1],
]


# P_from_g[1, 4] is a zero-one matrix.
lists_from_cube(P_from_g[1, 4]) == [
    [1, 0, 0, 0, 0, 1, 0, 0],
    [0, 1, 1, 0, 0, 0, 1, 0],
    [0, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 1],
]

# P_from_g[2, 3] is a zero-one matrix.
lists_from_cube(P_from_g[2, 3]) == [
    [1, 0, 0, 0, 0, 1, 0, 1],
    [0, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 1],
]

# P_from_g[3, 2] is rearrangement of P_from_g[2, 3] etc.


# Dimension 6.

# We skip P_from_g[0, 6] as it's the identity matrix.

# Here all zero-one, except for a single -1.
lists_from_cube(P_from_g[1, 5]) == [
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
    [0, 0, -1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
]

# Here all zero-one, except for two 2's and a single -2.
lists_from_cube(P_from_g[3, 3]) == [
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1],
    [0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
    [0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 2, 0, 0, 1, 2, 1, 0, 0, -2, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
]


# Code to pick out the non zero-one entries.
def doit(n):

    zero_one = set([0, 1])
    value = []
    for m in range(n + 1):
        ell = n - m
        if  m > ell:
            continue
        matrix = P_from_g[m, ell]
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
    (1, 5, 0, 6, 2, -1),
    (3, 3, 1, 1, 2, 2),
    (3, 3, 1, 1, 6, 2),
    (3, 3, 1, 1, 10, -2),
]

# The non zero-one entries for n = 7.
doit(7) == [
    (1, 6, 0, 6, 15, -1),
    (2, 5, 0, 6, 2, -1),
    (3, 4, 1, 1, 2, 2),
    (3, 4, 1, 1, 6, 2),
    (3, 4, 1, 1, 10, -2),
    (3, 4, 1, 1, 15, -2),
    (3, 4, 1, 2, 10, 2),
    (3, 4, 1, 2, 16, -2),
]

# For n = 8, 9, 10 just count how many entries.
len(doit(8)) == 45
len(doit(9)) == 127
len(doit(10)) == 530
