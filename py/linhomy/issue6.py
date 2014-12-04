from .issue4tools import cache_function
from .issue4tools import fib_zeros_array
from .issue4tools import enumerate_fib_suffix
from .constants import FIBWORDS
import re

ds_regex = re.compile(b'\x02+')


def fib_index(w):

    n = sum(w)
    return FIBWORDS[n].index(w)


def d_rule_1(v):
    # Suffix with a D.
    yield v + b'\x02'


def d_rule_2(v):

    if v.endswith(b'\x01'):

        for mo in ds_regex.finditer(v):

            start = mo.start()
            left, right = v[:start], v[start:]

            yield left + b'\x01' + right + b'\x01'


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


def c_rule_1(v):

    # Might not be any C in v.
    # Might like to write: if C not in v:
    if not b'\x01' in v:
        # GOTCHA: Wrote return value;
        yield b'\x01' + v      # Prefix with a C.
        raise StopIteration    # Could I use return instead?

    # Split at last C.
    left, right = v.rsplit(b'\x01', 1)

    # Join, inserting a C.
    yield left + b'\x01\x01' + right


def c_rule_2(v):

    if not v.endswith(b'\x02'):
        raise StopIteration

    # Split so tail is trailing D's.
    index = v.rfind(b'\x01') + 1
    base, d_tail = v[:index], v[index:]

    length = len(d_tail)
    for i in range(length, 0, -1):

        d_suffix = b'\x02' * i
        c_suffix = b'\x01\x01' * (length - i)
        yield base + c_suffix + d_suffix + b'\x01'


@cache_function
def _c_rule(cache, n):

    value = fib_zeros_array(n+1, n)

    for v in FIBWORDS[n]:

        for w in c_rule_1(v):
            value[fib_index(w), fib_index(v)] += 1

        for w in c_rule_2(v):
            value[fib_index(w), fib_index(v)] += 1

    return value


c_rule = _c_rule._cache
