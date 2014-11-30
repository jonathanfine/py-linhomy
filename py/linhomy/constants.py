import itertools
from linhomy.tools import cache_function


@cache_function
def _FIB(cache, n):
    '''Return n-th Fibonacci number 0, 1, 1, 2, 3, 5, 13, ...

    F(n) = F(n-1) + F(n-2) with F(0) = 1 and F(1) = 1.
    https://oeis.org/A000045
    '''

    if n >= 2:
        return cache[n-1] + cache[n-2]
    else:
        cache[0] = 0
        cache[1] = 1
        return cache[n]

FIB = _FIB._cache


@cache_function
def _FIBWORDS(cache, n):
    '''Tuple of all 1-2 words bytes that sum to n.

    Each word is a bytes object.  The length of FIBWORDS[n] is the
    Fibonacci number n+1.  The words are in lexicographic order.
    '''

    if n >= 2:
        return tuple(
            itertools.chain(
                map(b'\x01'.__add__, cache[n-1]),
                map(b'\x02'.__add__, cache[n-2]),
        ))
    else:
        cache[0] = (b'',)
        cache[1] = (b'\x01',)
        return cache[n]

FIBWORDS = _FIBWORDS._cache


@cache_function
def _CD_G_ONES(cache, n):

    # GOTCHA: Done to avoid nasty circular import.
    from .compute import cd_g_ones

    # TODO: Raise exception if n too large?
    if n > 10000:
        raise ValueError

    value = list(cd_g_ones(n))
    return value

CD_G_ONES = _CD_G_ONES._cache
