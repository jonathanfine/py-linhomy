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

# There's something wrong here.
P_stats(g_matrices_1, 2) == [(0, 2), (1, 4)]
P_stats(g_matrices_1, 3) == [(0, 7), (1, 8)]
P_stats(g_matrices_1, 4) == [(0, 35), (1, 25)]
P_stats(g_matrices_1, 5) == [(-1, 4), (0, 101), (1, 45), (2, 2)]
P_stats(g_matrices_1, 6) == [(-2, 2), (-1, 20), (0, 372), (1, 115), (2, 11)]
