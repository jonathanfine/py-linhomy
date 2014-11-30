import numpy as np
from .tools import cache_function
from .constants import FIB
from .constants import FIBWORDS
from .fibsubset import Word
from .fibtools import compute


@cache_function
def _CD_G(cache, n):

    shape = (FIB[n+1], FIB[n+1])
    value = np.zeros(shape, int)

    for i, w in enumerate(FIBWORDS[n]):
        # GOTCHA: Can't use shape.
        fib_shape = Word(w).worm.shape
        ones = compute(fib_shape)
        for v in ones:
            j = FIBWORDS[n].index(v)
            value[i, j] = 1

    return value

CD_G = _CD_G._cache


@cache_function
def _G_CD(cache, n):

    shape = (FIB[n+1], FIB[n+1])
    value = np.zeros(shape, int)

    g_cd = np.linalg.inv(CD_G[n])
    g_cd = np.rint(g_cd, value)

    return value

G_CD = _G_CD._cache
