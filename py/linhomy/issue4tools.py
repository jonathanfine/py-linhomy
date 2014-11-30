import numpy as np
from .tools import cache_function
from .constants import FIB
from .constants import FIBWORDS
from .fibsubset import Word
from .fibtools import compute


def linalg_int_inv(matrix):
    '''Compute the integer inverse of a matrix.'''

    shape = matrix.shape

    # Compute inverse and cast to integer matrix.
    tmp = np.linalg.inv(matrix)
    inverse = np.zeros(shape, int)
    inverse = np.rint(tmp, inverse)

    # Check we actually have the inverse.
    expect = np.eye(shape[0], dtype=int)
    actual = np.dot(matrix, inverse)
    if not np.array_equal(actual, expect):
        raise ValueError

    return inverse


def fib_zeros_array(*argv):
    '''Return array with shape (FIB[argv[0] + 1], ...).
    '''

    shape = tuple(FIB[n+1] for n in argv)
    value = np.zeros(shape, int)
    return value


@cache_function
def _CD_G(cache, n):

    value = fib_zeros_array(n, n)
    for i, w in enumerate(FIBWORDS[n]):
        shape = Word(w).worm.shape
        ones = compute(shape)
        for v in ones:
            j = FIBWORDS[n].index(v)
            value[i, j] = 1

    return value

CD_G = _CD_G._cache


@cache_function
def _G_CD(cache, n):

    return linalg_int_inv(CD_G[n])

G_CD = _G_CD._cache
