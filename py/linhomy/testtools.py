import numpy
from collections import Counter

# Copied from test issue25.py.
from .constants import FIBWORDS
def str_from_word(n, r):

    return ''.join(map(str, FIBWORDS[n][r]))

def P_stats(matrices, n):

    counter = Counter()
    for i in range(n+1):
        j = n - i
        if i <= j:
            mat = matrices.P_from_g[i, j]
            vec = numpy.reshape(mat, [-1])
            counter.update(vec)

    return sorted(counter.items())


# Copied from test issue25.py.
# Code to pick out the non zero-one entries.
def find_negatives(matrices, n):

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
