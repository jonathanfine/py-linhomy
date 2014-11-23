# 1. Compute the CD to g matrix
from linhomy.compute import cd_g_ones

# TODO: Same test code on constant.py and compute.py.
list(cd_g_ones(1)) == [
    (0, 0),
]

list(cd_g_ones(2)) == [
    (0, 0),
    (1, 1),
]

list(cd_g_ones(3)) == [
    (0, 0),
    (1, 1), (1, 2),
    (2, 2)
]

list(cd_g_ones(4)) == [
    (0, 0),
    (1, 1), (1, 2), (1, 3),
    (2, 2), (2, 3),
    (3, 3),
    (4, 4)
]

list(cd_g_ones(5)) == [
    (0, 0),
    (1, 1), (1, 2), (1, 3), (1, 5),
    (2, 2), (2, 3), (2, 5), (2, 7),
    (3, 3), (3, 5), (3, 6),
    (4, 4), (4, 6), (4, 7),
    (5, 5),
    (6, 6),
    (7, 7)
]
