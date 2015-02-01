from linhomy.matrices import G_matrices
from linhomy.testtools import P_stats
from linhomy.issue27 import g_from_CD_factory
from linhomy.issue28 import iter_contribute

g_from_CD_matrix, g_from_CD = g_from_CD_factory(iter_contribute)
g_matrices_1 = G_matrices(g_from_CD)

# These are pretty much as expected.  No negatives.
P_stats(g_matrices_1, 2) == [(0, 2), (1, 4)]
P_stats(g_matrices_1, 3) == [(0, 9), (1, 6)]
P_stats(g_matrices_1, 4) == [(0, 43), (1, 17)]
P_stats(g_matrices_1, 5) == [(0, 122), (1, 30)]
P_stats(g_matrices_1, 6) == [(0, 439), (1, 80), (2, 1)]

# n = 7. No negatives - a successful extrapolation.
P_stats(g_matrices_1, 7) == [(0, 1222), (1, 141), (2, 2)]

# n = 8. Two negatives - I wonder where and why.
P_stats(g_matrices_1, 8) == [(-1, 2), (0, 4058), (1, 349), (2, 11)]

# n = 9. Now have 18 negatives.
P_stats(g_matrices_1, 9) == [
    (-2, 1), (-1, 10),
    (0, 10884), (1, 630), (2, 24), (3, 1),
]

# n = 10. Now have 113 negatives.
P_stats(g_matrices_1, 10) == [
    (-2, 12), (-1, 78),
    (0, 34266), (1, 1506), (2, 90), (3, 4),
]

from linhomy.testtools import find_negatives

tmp = g_matrices_1.P_from_g
find_negatives(tmp, 6) == []
find_negatives(tmp, 7) == []
find_negatives(tmp, 8) == [
    (3, 5, 1, 4, 16, -1),
    (3, 5, 1, 6, 15, -1),
]


from linhomy.testtools import str_from_word

# Here are the sources of the exceptions.
# 8 = 3 + 5.
str_from_word(3, 1) == '12'     # '00:00'
str_from_word(5, 4) == '122'    # '00:10'
str_from_word(5, 6) == '212'    # '10:00'

# Here are the exceptions. They are the order 2 words that end with a
# '1'.

str_from_word(8, 15) == '121121' # '00:01:01' gives -1.
str_from_word(8, 16) == '121211' # '00:00:02' gives -1.


# Start to understand the negative values.

#   Let's unpack (3, 5, 1, 4, 16, -1).
list(g_matrices_1.CD_P_g[3, 5][1, 4]) == [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, -1,
    1, 1, 1, -1, 0, 1, 0, 1, -1, 0, 0, 0, -1, -1, 0, 1, 0,
]

list(g_matrices_1.g_from_CD[8][16,:]) == [
    0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1,
    1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
]


# Let's unpack (3, 5, 1, 6, 15, -1).
list(g_matrices_1.CD_P_g[3, 5][1, 6]) == [
    0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, 1, 0, 0, 1, 0, 1,
    0, -1, 0, 0, 0, 0, 1, -1, 0, 0, 2, -1, 0, -2, 0, 1, 0
]

list(g_matrices_1.g_from_CD[8][15,:]) == [
    0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0,
    0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
]


from linhomy.testtools import explain

# Either increase coefficient of 1, or change 0 to 1.  Don't yet see
# how to increase 1.  Do see opportunities for 0 to 1.

str_from_word(8, 15) == '121121' # '00:01:01' gives -1.
explain(g_matrices_1, 3, 5, 1, 6, 15) == [
    #                           # g_CD: explanation.
    ('112112', 1, -1, -1),      # 1: shift.
    ('112121', 1, -1, -1),      # 1: shift.
    ('112211', 0, 1, 0),        # 0: order.
    ('121112', 1, 1, 1),        # 1: shift.
    ('121211', 0, 1, 0),        # 0: can't shift back.
    ('122111', 0, -1, 0),       # 0: order.
    ('211121', 0, 1, 0),        # 0: order.
    ('211211', 0, -1, 0),       # 0: order.
    ('21212', 0, 2, 0),         # Perhaps '21212' -> '112121' -> '121121'.
    ('21221', 0, -1, 0),        # 0: order.
    ('22112', 0, -2, 0),        # 0: order.
    ('22211', 0, 1, 0),         # 0: order.
    # NOTE:  It's CD_P_g that's non-zero here, not g_P_g.
]

str_from_word(8, 16) == '121211' # '00:00:02' gives -1.
explain(g_matrices_1, 3, 5, 1, 4, 16) == [
    #                           # g_CD: explanation.
    ('121112', 1, -1, -1),      # 1: shift.
    ('121211', 1, -1, -1),      # 1: same.
    ('12122', 1, 1, 1),         # 1: promote '2' to '11'.
    ('122111', 0, 1, 0),        # 0: order.
    ('12212', 0, 1, 0),         # Perhaps '12212' -> '121121' -> '121211'.
    ('12221', 0, -1, 0),        # 0: order.
    ('211112', 0, 1, 0),        # 0: order.
    ('211211', 0, 1, 0),        # 0: order.
    ('21122', 0, -1, 0),        # 0: order.
    ('221111', 0, -1, 0),       # 0: order.
    ('22112', 0, -1, 0),        # 0: order.
    ('22211', 0, 1, 0),         # 0: order.
    # NOTE:  It's CD_P_g that's non-zero here, not g_P_g.
]
