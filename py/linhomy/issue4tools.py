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


@cache_function
def _C_CD(cache, n):

    value = fib_zeros_array(n+1, n)

    for j, w in enumerate(FIBWORDS[n]):

        # Compute index i for 'Cw' and set value[i, j].
        v = w + b'\x01'
        i = FIBWORDS[n+1].index(v)
        value[i, j] = 1

    return value

C_CD = _C_CD._cache


@cache_function
def _D_CD(cache, n):

    value = fib_zeros_array(n+2, n)

    for j, w in enumerate(FIBWORDS[n]):

        # Compute index i for 'Dw' and set value[i, j].
        v = w + b'\x02'
        i = FIBWORDS[n+2].index(v)
        value[i, j] = 1

    return value

D_CD = _D_CD._cache


@cache_function
def _C_G(cache, n):

    curr = G_CD[n]                 # Convert to CD basis.
    curr = np.dot(C_CD[n], curr)   # Bump dimension.
    curr = np.dot(CD_G[n+1], curr) # Return to G basis.

    return curr

C_G = _C_G._cache


@cache_function
def _D_G(cache, n):

    curr = G_CD[n]                 # Convert to CD basis.
    curr = np.dot(D_CD[n], curr)   # Bump dimension.
    curr = np.dot(CD_G[n+2], curr) # Return to G basis.

    return curr

D_G = _D_G._cache


# TODO: Rename and test.
def wibble(s):

    return Word(s).worm.shape.arg


# TODO: Test.
def non_zero_entries(matrix):

    n_fib, m_fib = matrix.shape
    if n_fib == 1 or m_fib == 1:
        raise ValueError

    tmp = [FIB[0]]
    while tmp[-1] < max(n_fib, m_fib):
        tmp.append(FIB[len(tmp)])

    n = tmp.index(n_fib) - 1
    m = tmp.index(m_fib) - 1

    for j in range(m_fib):
        for i in range(n_fib):
            coeff = matrix[i, j]
            if coeff:
                i_word = FIBWORDS[n][i]
                j_word = FIBWORDS[m][j]
                yield j_word, i_word, coeff


# TODO: Test - but printing to stdout is yuck.
def print_entries(entries):

    for j_word, i_word, coeff in entries:

        i_str = wibble(i_word)
        j_str = wibble(j_word)

        coeff = '{0:+}'.format(coeff)
        print(coeff, j_str, i_str)
