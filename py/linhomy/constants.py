import itertools
from linhomy.tools import self_extending_list


@self_extending_list([0, 1])
def FIB(self, key):
    '''The Fibonacci numbers 0, 1, 1, 2, 3, 5, 13, ...

    F(n) = F(n-1) + F(n-2) with F(0) = 1 and F(1) = 1.
    https://oeis.org/A000045
    '''

    return [self[-1] + self[-2]]


@self_extending_list([
    (b'',),
    (b'\x01',),
])
def FIBWORDS(self, key):
    '''Tuple of all 1-2 words bytes that sum to key.

    Each word is a bytes object.  The length of FIBWORD[n] is the
    Fibonacci number n+1.  The words are in lexicographic order.
    '''

    # GOTCHA: Return a list containing a single item.
    return [tuple(
        itertools.chain(
            map(b'\x01'.__add__, self[-1]),
            map(b'\x02'.__add__, self[-2]),
        ))]


@self_extending_list([])
def CD_G_ONES(self, key):

    # GOTCHA: Done to avoid nasty circular import.
    from .compute import cd_g_ones

    # TODO: This is just until we have properly cached values.
    if key > 10:
        raise ValueError

    length = len(self)
    value = list(cd_g_ones(length))
    return [value]
