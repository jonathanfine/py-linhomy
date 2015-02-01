from linhomy.matrices import G_matrices
from linhomy.testtools import P_stats
from linhomy.issue27 import g_from_CD_factory
from linhomy.issue29 import iter_contribute

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
P_stats(g_matrices_1, 8) == [(0, 4056), (1, 352), (2, 12)]

# n = 9. Now have 5 negatives.
P_stats(g_matrices_1, 9) == [
    (-2, 2), (-1, 3),
    (0, 10870), (1, 644), (2, 27), (3, 4),
]

# n = 10. Now have 118 negatives.
P_stats(g_matrices_1, 10) == [
    (-5, 1), (-4, 1), (-3, 3), (-2, 31), (-1, 82),
    (0, 34170), (1, 1541), (2, 112), (3, 15),
]

from linhomy.testtools import find_negatives

tmp = g_matrices_1.P_from_g
find_negatives(tmp, 6) == []
find_negatives(tmp, 7) == []
find_negatives(tmp, 8) == [
#    (3, 5, 1, 4, 16, -1),
#    (3, 5, 1, 6, 15, -1),
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
    1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
]


# Let's unpack (3, 5, 1, 6, 15, -1).
list(g_matrices_1.CD_P_g[3, 5][1, 6]) == [
    0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, 1, 0, 0, 1, 0, 1,
    0, -1, 0, 0, 0, 0, 1, -1, 0, 0, 2, -1, 0, -2, 0, 1, 0
]

list(g_matrices_1.g_from_CD[8][15,:]) == [
    0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0,
    0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0
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
    ('21212', 1, 2, 2),         # Perhaps '21212' -> '112121' -> '121121'.
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
    ('12212', 1, 1, 1),         # Perhaps '12212' -> '121121' -> '121211'.
    ('12221', 0, -1, 0),        # 0: order.
    ('211112', 0, 1, 0),        # 0: order.
    ('211211', 0, 1, 0),        # 0: order.
    ('21122', 0, -1, 0),        # 0: order.
    ('221111', 0, -1, 0),       # 0: order.
    ('22112', 0, -1, 0),        # 0: order.
    ('22211', 0, 1, 0),         # 0: order.
    # NOTE:  It's CD_P_g that's non-zero here, not g_P_g.
]

find_negatives(tmp, 9) == [
    (1, 8, 0, 27, 23, -1),
    (4, 5, 1, 6, 24, -2),
    (4, 5, 1, 6, 42, -1),
    (4, 5, 1, 6, 44, -2),
    (4, 5, 1, 6, 45, -1),
]


str_from_word(9, 23) == '1211121'
# TODO: This is odd - dimension 9 = 1 + 8.
explain(g_matrices_1, 1, 8, 0, 27, 23) == [
    ('1112112', 1, -1, -1),     # 1: shift.
    ('1112211', 0, 1, 0),       # 0: order.
    ('1121112', 1, 1, 1),       # 1: shift.
    ('1121121', 1, -1, -1),     # 1: shift.
    ('1121211', 0, 1, 0),       # 0: can't shift.
    ('1122111', 0, -1, 0),      # 0: order.
    ('2111121', 0, 1, 0),       # 0: order.
    ('2111211', 0, -1, 0),      # 0: order.
    ('211212', 1, 1, 1),        # 1: vec == [1, 0, 0].
    ('211221', 0, -1, 0),       # 0: order.
    # TODO: Is there a way to exclude this?
    ('212112', 1, -1, -1),      # 1: vec == [1, 0, 0].
    ('212211', 0, 1, 0),        # 0: order.
]


str_from_word(9, 24) == '1211211'
explain(g_matrices_1, 4, 5, 1, 6, 24) == [
    ('1112112', 1, -1, -1),     # 1: shift.
    ('1112121', 1, -1, -1),     # 1: shift.
    ('1112211', 0, 1, 0),       # 0: order.
    ('1121112', 1, 1, 1),       # 1: shift.
    ('1121121', 1, 2, 2),       # 1: shift.
    ('1121211', 1, 1, 1),       # 1: shift.
    ('1122111', 0, -2, 0),      # 0: order.
    ('1211121', 1, -1, -1),     # 1: shift.
    ('1211211', 1, -1, -1),     # 1: same.
    ('1221111', 0, 1, 0),       # 0: order.
    ('211212', 1, 2, 2),        # 1: vec [1, 0, 0].
    ('211221', 0, -1, 0),       # 0: order.
    # TODO: Is there a way to exclude these two?
    ('212112', 1, -2, -2),      # 1: vec [1, 0, 0].
    ('212121', 1, -2, -2),      # 1: vec [1, 0, 0].
    ('212211', 0, 2, 0),        # 0: order.
    ('221121', 0, 2, 0),        # 0: order.
    ('222111', 0, -1, 0),       # 0: order.
]

str_from_word(9, 42) == '2121111'
# TODO: This one seems hard to explain.
explain(g_matrices_1, 4, 5, 1, 6, 42) == [
    ('1112112', 1, -1, -1),
    ('1112121', 1, -1, -1),
    ('1112211', 0, 1, 0),
    ('1121112', 1, 1, 1),
    ('1121121', 1, 2, 2),
    ('1121211', 1, 1, 1),
    ('1122111', 0, -2, 0),
    ('1211121', 1, -1, -1),
    ('1211211', 1, -1, -1),
    ('1221111', 0, 1, 0),
    ('211212', 1, 2, 2),
    ('211221', 1, -1, -1),
    ('212112', 1, -2, -2),
    ('212121', 1, -2, -2),
    ('212211', 1, 2, 2),
    ('221121', 0, 2, 0),
    ('222111', 0, -1, 0),
]

str_from_word(9, 44) == '212121'
explain(g_matrices_1, 4, 5, 1, 6, 44) == [
    ('1112112', 0, -1, 0),
    ('1112121', 0, -1, 0),
    ('1112211', 0, 1, 0),
    ('1121112', 0, 1, 0),
    ('1121121', 0, 2, 0),
    ('1121211', 0, 1, 0),
    ('1122111', 0, -2, 0),
    ('1211121', 0, -1, 0),
    ('1211211', 0, -1, 0),
    ('1221111', 0, 1, 0),
    ('211212', 1, 2, 2),
    ('211221', 0, -1, 0),
    ('212112', 1, -2, -2),
    ('212121', 1, -2, -2),
    ('212211', 0, 2, 0),
    ('221121', 0, 2, 0),
    ('222111', 0, -1, 0),
]

str_from_word(9, 45) == '212211'
explain(g_matrices_1, 4, 5, 1, 6, 45) == [
    ('1112112', 0, -1, 0),
    ('1112121', 0, -1, 0),
    ('1112211', 0, 1, 0),
    ('1121112', 0, 1, 0),
    ('1121121', 0, 2, 0),
    ('1121211', 0, 1, 0),
    ('1122111', 0, -2, 0),
    ('1211121', 0, -1, 0),
    ('1211211', 0, -1, 0),
    ('1221111', 0, 1, 0),
    ('211212', 1, 2, 2),
    ('211221', 1, -1, -1),
    ('212112', 1, -2, -2),
    ('212121', 1, -2, -2),
    ('212211', 1, 2, 2),
    ('221121', 0, 2, 0),
    ('222111', 0, -1, 0),
]
