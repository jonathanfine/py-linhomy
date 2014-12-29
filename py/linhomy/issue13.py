import itertools
import numpy
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
