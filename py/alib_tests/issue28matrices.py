from linhomy.matrices import G_matrices
from linhomy.testtools import P_stats
from linhomy.issue27 import g_from_CD_factory
from linhomy.issue28 import iter_contribute

g_matrices_1 = G_matrices(g_from_CD_factory(iter_contribute)[1])

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

# n = 9. Now have 11 negatives.
P_stats(g_matrices_1, 9) == [
    (-2, 1), (-1, 10),
    (0, 10884), (1, 630), (2, 24), (3, 1),
]

# n = 10. Now have 90 negatives.
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

# 8 = 4 + 4.
str_from_word(4, 1) == '112'    # '01:00'


# Here are the exceptions. They are the order 2 words that end with a
# '1'.
str_from_word(8, 15) == '121121' # '00:01:01' gives -1.
str_from_word(8, 16) == '121211' # '00:00:02' gives -1.
