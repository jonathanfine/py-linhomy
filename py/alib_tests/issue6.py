import numpy as np
from linhomy.issue6 import d_rule
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
