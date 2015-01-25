from collections import Counter
import numpy
from linhomy.matrices import G_matrices


def P_stats(matrices, n):

    counter = Counter()
    for i in range(n+1):
        j = n - i
        if i <= j:
            mat = matrices.P_from_g[i, j]
            vec = numpy.reshape(mat, [-1])
            counter.update(vec)

    return sorted(counter.items())


from linhomy.issue27 import g_from_CD_1
g_matrices_1 = G_matrices(g_from_CD_1)

# These are pretty much as expected.  No negatives.
P_stats(g_matrices_1, 2) == [(0, 2), (1, 4)]
P_stats(g_matrices_1, 3) == [(0, 9), (1, 6)]
P_stats(g_matrices_1, 4) == [(0, 43), (1, 17)]
P_stats(g_matrices_1, 5) == [(0, 122), (1, 30)]
P_stats(g_matrices_1, 6) == [(0, 439), (1, 80), (2, 1)]

# n = 7. No negatives - a successful extrapolation.
P_stats(g_matrices_1, 7) == [(0, 1222), (1, 141), (2, 2)]

# n = 8. Four negatives - I wonder where and why.
P_stats(g_matrices_1, 8) == [(-2, 2), (-1, 2), (0, 4058), (1, 347), (2, 11)]

# n = 9. Now have 18 negatives.
P_stats(g_matrices_1, 9) == [
    (-2, 7), (-1, 11),
    (0, 10886), (1, 624), (2, 21), (3, 1),
]

# n = 10. Now have 113 negatives.
P_stats(g_matrices_1, 10) == [
    (-4, 2), (-3, 1), (-2, 32), (-1, 77),
    (0, 34282), (1, 1478), (2, 80), (3, 4),
]


# Copied from test issue25.py.
# Code to pick out the non zero-one entries.
def doit(matrices, n):

    zero_one = set([0, 1])
    value = []
    for m in range(n + 1):
        ell = n - m
        if  m > ell:
            continue
        matrix = matrices[m, ell]
        # TODO: provide an 'enumerate' for numpy matrices.
        i_lim, j_lim, k_lim = matrix.shape
        for i in range(i_lim):
            for j in range(j_lim):
                for k in range(k_lim):
                    c = matrix[i, j, k]
                    if c < 0:
                        value.append((m, ell, i, j, k, c))

    return value

tmp = g_matrices_1.P_from_g
doit(tmp, 6) == []
doit(tmp, 7) == []
doit(tmp, 8) == [
    (3, 5, 1, 4, 16, -1),
    (3, 5, 1, 6, 10, -2),
    (3, 5, 1, 6, 15, -1),
    (4, 4, 1, 1, 10, -2),
]

# Copied from issue25.py.
from linhomy.constants import FIBWORDS
def str_from_word(n, r):

    return ''.join(map(str, FIBWORDS[n][r]))


# Here are the sources of the exceptions.
# 8 = 3 + 5.
str_from_word(3, 1) == '12'     # '00:00'
str_from_word(5, 4) == '122'    # '00:10'
str_from_word(5, 6) == '212'    # '10:00'

# 8 = 4 + 4.
str_from_word(4, 1) == '112'    # '01:00'


# Here are the exceptions. They are the order 2 words that end with a
# '1'.
str_from_word(8, 10) == '112121' # '01:00:01' gives -2 (two ways).
str_from_word(8, 15) == '121121' # '00:01:01' gives -1.
str_from_word(8, 16) == '121211' # '00:00:02' gives -1.
