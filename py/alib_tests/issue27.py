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

# n = 8. Only three negatives - I wonder where and why.
P_stats(g_matrices_1, 8) == [(-2, 2), (-1, 2), (0, 4058), (1, 347), (2, 11)]

# n = 9. Still only three negatives.
P_stats(g_matrices_1, 9) == [
    (-2, 7), (-1, 11),
    (0, 10886), (1, 624), (2, 21), (3, 1),
]

# n = 10. A small leap, to 10 negatives.
P_stats(g_matrices_1, 10) == [
    (-4, 2), (-3, 1), (-2, 32), (-1, 77),
    (0, 34282), (1, 1478), (2, 80), (3, 4),
]
