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
