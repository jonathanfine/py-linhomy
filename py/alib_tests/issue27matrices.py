from linhomy.issue26 import iter_contribute
from linhomy.issue27 import g_from_CD_matrix


def lists_from_matrix(matrix):

    return [
        list(map(int, row))
        for row in matrix
    ]


# Check that iter_contribute does the right thing.

# Simple (order zero).
list(iter_contribute([[0, 4]])) == [[[0, 4]]] # CCCC.
list(iter_contribute([[1, 2]])) == [[[1, 2]]] # DC.
list(iter_contribute([[2, 0]])) == [[[2, 0]]] # DD.

# Order one.
# CDC -> CDC, DCC.
list(iter_contribute([[0, 0], [0, 1]])) == [
    [[0, 0], [0, 1]],
    [[1, 2]],
]

# CCD -> CCD, CDC, DCC.
list(iter_contribute([[0, 1], [0, 0]])) == [
    [[0, 1], [0, 0]],
    [[0, 0], [0, 1]],
    [[1, 2]],
]


from linhomy.issue27 import fibword_from_pairs
from linhomy.issue27 import pairs_from_fibword
from linhomy.constants import FIBWORDS

# There's something wrong here.
fibword_from_pairs(pairs_from_fibword(bytes([1, 2]))) == bytes([1, 2])
fibword_from_pairs(pairs_from_fibword(bytes([2, 1]))) == bytes([2, 1])

fibword_from_pairs(pairs_from_fibword(bytes([1, 1, 2]))) == bytes([1, 1, 2])
fibword_from_pairs(pairs_from_fibword(bytes([2, 1, 1]))) == bytes([2, 1, 1])

# These two are correct.
pairs_from_fibword(bytes([1, 2])) == [(0, 0), (0, 0)]
pairs_from_fibword(bytes([2, 1])) == [(1, 1)]


# This succeeds.
for w in FIBWORDS[4]:
    (w, fibword_from_pairs(pairs_from_fibword(w))) == (w, w)


# This is correct value - see test matrices.py CD_from_g[4].
lists_from_matrix(g_from_CD_matrix(4)) == [
    [1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 1],
]


# We will discover if there are double counts.
def find_double_counts(n):
    value = []
    for i, w in enumerate(FIBWORDS[n]):

        contrib = list(iter_contribute(pairs_from_fibword(w)))
        contrib = tuple(
            tuple(
                tuple(pair)
                for pair in pairs
            )
            for pairs in contrib
        )

        double_counts = len(contrib) - len(set(contrib))

        if double_counts:
            value.append((i, double_counts, len(contrib)))

    return value

# These are OK.
find_double_counts(2) == []
find_double_counts(3) == []
find_double_counts(4) == []
find_double_counts(5) == []
find_double_counts(6) == []

# Here there are double counts - so perhap results are wrong.
find_double_counts(7) == [
    (6, 1, 14),
]

find_double_counts(8) == [
    (6, 2, 21),
    (9, 1, 18),
    (10, 1, 14),
]
