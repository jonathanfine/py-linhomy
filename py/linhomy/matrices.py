import itertools
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


def IC_from_CD_helper(cd_word):

    pending = []
    for piece in cd_word.split(b'\x02'):
        if piece:
            pending.append((piece,))

        pending.append((b'\x01\x01', b'\x02'))

    del pending[-1]

    for items in itertools.product(*pending):
        yield b''.join(items)
