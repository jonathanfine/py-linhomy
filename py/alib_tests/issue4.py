from linhomy.issue4tools import CD_G
from linhomy.issue4tools import G_CD
from linhomy.issue4tools import C_CD
from linhomy.issue4tools import D_CD
from linhomy.issue4tools import C_G
from linhomy.issue4tools import D_G

from linhomy.issue4tools import linalg_int_inv  # TODO: Add tests.
from linhomy.issue4tools import fib_zeros_array # TODO: Add tests.

def aaa(matrix):
    return list(map(list, matrix))

aaa(CD_G[4]) == [
    [1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 1, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1],
]

aaa(G_CD[4]) == [
    [1, 0, 0, 0, 0],
    [0, 1, -1, 0, 0],
    [0, 0, 1, -1, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1],
]

aaa(C_CD[4]) == [
    [1, 0, 0, 0, 0],            #
    [0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0],            #
    [0, 0, 1, 0, 0],            #
    [0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0],            #
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1],            #
]

aaa(D_CD[4]) == [
    [0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0],            #
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0],            #
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0],            #
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0],            #
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1],            #
]

aaa(C_G[4]) == [
    [1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 0, 0, 1],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1],
]

aaa(D_G[4]) == [
    [0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1],
]

## From rules for C and D construct g_from_cd function.

from linhomy.issue4tools import g_from_cd_rules_factory
from linhomy.issue4tools import C_G, D_G, CD_G
import numpy as np


AAA = g_from_cd_rules_factory(C_G, D_G)._cache
for n in range(6):
    np.array_equal(AAA[5], CD_G[5]) == True
