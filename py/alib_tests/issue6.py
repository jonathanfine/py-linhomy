import numpy as np
from linhomy.issue6 import c_rule
from linhomy.issue6 import d_rule
from linhomy.issue4tools import g_from_cd_rules_factory
from linhomy.issue4tools import C_G
from linhomy.issue4tools import D_G


def do_d_rule(n):

    aaa = d_rule[n]
    bbb = D_G[n]
    diff = np.nonzero(aaa - bbb)

    indices = list(zip(*diff))

    # TODO: Display differences more usefully.
    return indices

do_d_rule(0) == []
do_d_rule(1) == []
do_d_rule(2) == []
do_d_rule(3) == []
do_d_rule(4) == []
do_d_rule(5) == []
do_d_rule(6) == [(3, 10), (24, 10)]
do_d_rule(7) == [
    (3, 10), (3, 15), (5, 16), (24, 10),
    (24, 15), (37, 15), (39, 16)
]


def do_c_rule(n):

    aaa = c_rule[n]
    bbb = C_G[n]
    diff = np.nonzero(aaa - bbb)

    indices = list(zip(*diff))

    # TODO: Display differences more usefully.
    return indices


do_c_rule(0) == []
do_c_rule(1) == []
do_c_rule(2) == []
do_c_rule(3) == []
do_c_rule(4) == []
do_c_rule(5) == [(3, 6), (6, 6)]
do_c_rule(6) == [(3, 6), (3, 10), (6, 6)]
do_c_rule(7) == [
    (3, 6), (3, 10), (5, 17), (6, 6),
    (9, 17), (11, 19), (17, 17), (19, 19)
]


g_from_cd = g_from_cd_rules_factory(c_rule, d_rule)

def do_g_from_cd(n):
    '''Check that computed g_from_cd is all ones.
    '''

    matrix = g_from_cd(n)

    r, s = matrix.shape
    count = 0
    errors = 0

    for i in range(r):
        for j in range(s):

            entry = matrix[i, j]
            if not(entry == 0 or entry == 1):
                errors += 1

            if entry == 1:
                count += 1

    return count, errors


# Check that computed g_from_cd is all ones.
do_g_from_cd(0) == (1, 0)
do_g_from_cd(1) == (1, 0)
do_g_from_cd(2) == (2, 0)
do_g_from_cd(3) == (4, 0)
do_g_from_cd(4) == (8, 0)
do_g_from_cd(5) == (18, 0)
do_g_from_cd(6) == (40, 0)
do_g_from_cd(7) == (91, 0)

# One failure, here it is.
do_g_from_cd(8) == (206, 1)
g_from_cd(8)[3, 27] == 2


# Six failures, here they are.
do_g_from_cd(9) == (464, 6)

g_from_cd(9)[3, 27] == 2
g_from_cd(9)[3, 40] == 3
g_from_cd(9)[3, 43] == 2
g_from_cd(9)[5, 43] == 2
g_from_cd(9)[5, 44] == 2
g_from_cd(9)[23, 41] == 2
