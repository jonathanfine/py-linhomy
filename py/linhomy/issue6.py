from .issue4tools import cache_function
from .issue4tools import fib_zeros_array
from .issue4tools import enumerate_fib_suffix
from .constants import FIBWORDS

def fib_index(w):

    n = sum(w)
    return FIBWORDS[n].index(w)


def d_rule_1(v):
    # Suffix with a D.
    yield v + b'\x02'


def d_rule_2(v):

    if v.endswith(b'\x01'):

        v_split = v.split(b'\x02\x01')
        for i in range(len(v_split) - 1):

            left = b'\x02\x01'.join(v_split[:i])
            right = b'\x02\x01'.join(v_split[i:-1])
            tail = v_split[-1]

            # GOTCHA: Why is it obvious that this is correct?XS
            yield left + b'\x01' + right + b'\x02\x01' + b'\x01' + tail


@cache_function
def _d_rule(cache, n):

    value = fib_zeros_array(n+2, n)

    for v in FIBWORDS[n]:

        for w in d_rule_1(v):
            value[fib_index(w), fib_index(v)] += 1

        for w in d_rule_2(v):
            value[fib_index(w), fib_index(v)] += 1

    return value


d_rule = _d_rule._cache
