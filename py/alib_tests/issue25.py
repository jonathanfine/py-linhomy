import numpy

from linhomy.cdrules import g_from_CD_factory

from linhomy.issue25 import c_rule
from linhomy.issue25 import d_rule

from linhomy.matrices import G_matrices

MAX = 6
g_matrices = G_matrices(g_from_CD_factory(c_rule, d_rule), max=MAX)
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


# P_from_g[1, 4] is zero-one matrix.
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


doit(5) == []


# The non zero-one entries for n = 6.
doit(6) == [
    (3, 3, 1, 1, 3, -2),
    (3, 3, 1, 1, 6, 2),
    (3, 3, 1, 1, 10, -2),
]


# Let's look at these non-boolean entries.
from linhomy.constants import FIBWORDS
from linhomy.cdrules import Index

def str_from_word(n, r):

    return ''.join(map(str, FIBWORDS[n][r]))

# All exceptions are from ':00' x ':00'
str_from_word(3, 1) == '12'     # ':00'

# Here are the exceptions.
str_from_word(6, 3) == '11211'  # '01:02' gives -2.
str_from_word(6, 6) == '1212'   # ':00:00' gives 2.
str_from_word(6, 10) == '2121'  # '10:01' gives -2.

# ':00:00' represents a double collapsing. In ':00' x ':00' there are
# two ways to get a double collapsing, by taking one or the other
# factor first.  So the coefficient 2 for ':00:00' is correct.


from linhomy.matrices import P_from_CD

str_from_word(3, 0) == '111'
str_from_word(3, 1) == '12'
str_from_word(3, 2) == '21'
list(g_matrices.CD_from_g[3][1,:]) == [0, 1, 0]
list(g_matrices.CD_from_g[3][:,1]) == [0, 1, -1]

list(P_from_CD[3, 3][1, 1]) == [0, 0, 0, 0, 0, 0, 2, -1, 0, 0, 0, 0, 1]
list(P_from_CD[3, 3][1, 2]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1]
list(P_from_CD[3, 3][2, 2]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1]

# The CD vector for ':00' x ':00'.  We can't change this.
cd_of_product = [0, 0, 0, 0, 0, 0, 2, -1, 0, -2, 0, 1, 0]
list(
    P_from_CD[3, 3][1, 1]
    -P_from_CD[3, 3][1, 2]
    -P_from_CD[3, 3][2, 1]
    +P_from_CD[3, 3][2, 2]
) == cd_of_product


# Non-zero coefficients in more explicit form.
[
    (r, str_from_word(6, r), s)
    for r, s in enumerate(cd_of_product)
    if s != 0
] == [
    (6, '1212', 2),
    (7, '1221', -1),
    (9, '2112', -2),
    (11, '2211', 1),
]

# Line up to see how product works.                       6   7      9    11.
cd_of_product ==                       [0, 0, 0, 0, 0, 0, 2, -1, 0, -2, 0, 1, 0]
list(g_matrices.g_from_CD[6][6,:]) ==  [0, 0, 0, 0, 0, 0, 1,  0, 0,  0, 0, 0, 0]
list(g_matrices.g_from_CD[6][3,:]) ==  [0, 1, 1, 1, 1, 0, 0,  0, 0,  1, 1, 0, 0]
list(g_matrices.g_from_CD[6][10,:]) == [0, 0, 0, 0, 0, 0, 0,  0, 0,  1, 1, 0, 0]

# Let's check the calculation. Here are the exceptions (again).

# Here we meet at index 6, to get 2.
str_from_word(6, 6) == '1212'   # ':00:00' gives 2.

# Here we meet at index 9, to get -2.
str_from_word(6, 3) == '11211'  # '01:02' gives -2.
str_from_word(6, 10) == '2121'  # '10:01' gives -2.

# We can now look at these calculations as see how the non-booleans
# might be avoided.
