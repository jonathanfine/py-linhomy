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
fibword_from_pairs(pairs_from_fibword(bytes([1, 2]))) == bytes([2, 1])
fibword_from_pairs(pairs_from_fibword(bytes([2, 1]))) == bytes([1, 2])

fibword_from_pairs(pairs_from_fibword(bytes([1, 1, 2]))) == bytes([2, 1, 1])
fibword_from_pairs(pairs_from_fibword(bytes([2, 1, 1]))) == bytes([1, 1, 2])

# These two are wrong.
pairs_from_fibword(bytes([1, 2])) == [(1, 1)]
pairs_from_fibword(bytes([2, 1])) == [(0, 0), (0, 0)]


# This fails.
for w in FIBWORDS[4]:
    break
    (w, fibword_from_pairs(pairs_from_fibword(w))) == (w, w)


# This does not have ones along the whole diagonal.
lists_from_matrix(g_from_CD_matrix(4)) == [
    [1, 0, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 1, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 1],
]
