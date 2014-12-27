from .constants import FIBWORDS
from .data import _cache
from .data import replace_12_CIC
from .issue4tools import fib_zeros_array


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
