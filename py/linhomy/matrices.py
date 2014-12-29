import itertools
import numpy
from .cdrules import g_from_CD_helper
from .cdrules import fibword_from_index
from .constants import FIB
from .constants import FIBWORDS
from .data import _cache
from .data import replace_12_CIC
from .issue4tools import fib_zeros_array
from .issue4tools import linalg_int_inv


def _F_from_IC(n):

    words = FIBWORDS[n]
    value = fib_zeros_array(n, n)

    for i, w in enumerate(words):
        ic_word = replace_12_CIC(w)
        value[i,:] = _cache[ic_word]

    return value


F_from_IC = [
    _F_from_IC(n)
    for n in range(11)
]

IC_from_F = list(map(linalg_int_inv, F_from_IC))


def IC_from_CD_helper(cd_word):

    pending = []
    for piece in cd_word.split(b'\x02'):
        if piece:
            pending.append((piece,))

        pending.append((b'\x01\x01', b'\x02'))

    del pending[-1]

    for items in itertools.product(*pending):
        yield b''.join(items)


def _IC_from_CD(n):

    value = fib_zeros_array(n, n)
    words = FIBWORDS[n]

    for i, w in enumerate(words):
        for v in IC_from_CD_helper(w):
            j = words.index(v)
            value[i, j] += 1

    return value


IC_from_CD =  [
    _IC_from_CD(n)
    for n in range(11)
]

CD_from_IC = list(map(linalg_int_inv, IC_from_CD))


def _g_from_CD(n):

    words = FIBWORDS[n]
    value = fib_zeros_array(n, n)

    for i, v in enumerate(words):
        for w_index in g_from_CD_helper(v):
            w_fibword = fibword_from_index(w_index)
            j = words.index(w_fibword)
            value[i,j] += 1

    return value


g_from_CD = [
    _g_from_CD(n)
    for n in range(11)
]

CD_from_g = list(map(linalg_int_inv, g_from_CD))


def _J_from_IC(n, m):

    value = fib_zeros_array(n, m, n + m + 1)
    for i, v in enumerate(FIBWORDS[n]):
        for j, w in enumerate(FIBWORDS[m]):

            # Prepare to look up flag vector of join.
            v_IC = replace_12_CIC(v)
            w_IC = replace_12_CIC(w)
            join_word = b'J(' + v_IC + b',' + w_IC + b')'

            # Look up join flag vector, convert to IC vector.
            join_flag = _cache[join_word]
            join_ic = numpy.dot(IC_from_F[n+m+1], join_flag)
            value[i, j, :] = join_ic

    return value


J_from_IC = dict(
    ((n, m),  _J_from_IC(n, m))
    for n in range(11)
    for m in range(11 - n - 1)
)


def _J_from_CD(n, m):

    value = fib_zeros_array(n, m, n + m + 1)
    matrix = J_from_IC[n, m]
    rows = numpy.reshape(matrix, (FIB[n+1] * FIB[m+1], -1))

    for i, v in enumerate(FIBWORDS[n]):
        for j, w in enumerate(FIBWORDS[m]):

            coefficients = [
                r * s
                for r in IC_from_CD[n][i]
                for s in IC_from_CD[m][j]
            ]

            join_ic = sum(
                c * r
                for (c, r) in zip(coefficients, rows)
            )

            join_cd = numpy.dot(CD_from_IC[n+m+1], join_ic)
            value[i, j, :] = join_cd

    return value


J_from_CD = dict(
    ((n, m),  _J_from_CD(n, m))
    for n in range(11)
    for m in range(11 - n - 1)
)
