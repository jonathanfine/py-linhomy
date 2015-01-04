import os
from linhomy.data import _DATAPATH

_DATAPATH.endswith('linhomy/_data') == True
os.path.abspath(_DATAPATH) == _DATAPATH


from linhomy.data import read_data

# This is fairly regular.
read_data('IC-{0}-flag.txt', 0) == b'p 1\n'
read_data('IC-{0}-flag.txt', 1) == b'C 1\n'
read_data('IC-{0}-flag.txt', 2) == b'CC 1 3\nIC 1 4\n'
read_data('P-{0}-flag.txt', 0) == b''
read_data('P-{0}-flag.txt', 1) == b''
read_data('P-{0}-flag.txt', 2) == b'P(C,C) 1 4\n'
read_data('P-{0}-flag.txt', 3) == b'P(C,CC) 1 6 9\nP(C,IC) 1 8 12\n'


# This is odd.  Skipping join where one factor is 'C' * n.
# TODO: How to import FileNotFoundError, which is real exception?
read_data('J-{0}-flag.txt', 0) == b''
read_data('J-{0}-flag.txt', 1) == b''
read_data('J-{0}-flag.txt', 2) == b''
read_data('J-{0}-flag.txt', 3) == b''
read_data('J-{0}-flag.txt', 4) == b''
read_data('J-{0}-flag.txt', 5) == b'J(IC,IC) 1 8 24 34 104 24 104 160\n'


from linhomy.data import _cache

_cache[b'DNE'] ** ValueError
# len(_cache) == 0                # Can fail due to side effects.

_cache[b''] == (1,)
# len(_cache) == 1                # Can fail due to side effects.

_cache[b'I'] ** ValueError
_cache[b'C'] == (1,)
# len(_cache) == 1 + 1            # Can fail due to side effects.

_cache[b'CC'] == (1, 3)
_cache[b'IC'] == (1, 4)
# len(_cache) == 1 + 1 + 2        # Can fail due to side effects.

_cache[b'CCC'] == (1, 4, 6)
# len(_cache) == 1 + 1 + 2 + 3    # Can fail due to side effects.

_cache[b'CCCC'] == (1, 5, 10, 10, 30)
# len(_cache) == 1 + 1 + 2 + 3 + 5 # Can fail due to side effects.


# Join.
from linhomy.data import twiddle

twiddle(b'J', b'J(ICC,IC)') == b'J(IC,ICC)'
twiddle(b'J', b'J(IC,ICC)') == b'J(ICC,IC)'
twiddle(b'P', b'P(ICC,IC)') == b'P(IC,ICC)'
twiddle(b'P', b'P(IC,ICC)') == b'P(ICC,IC)'

_cache[b'J(IC,IC)'] == (1, 8, 24, 34, 104, 24, 104, 160)
_cache[b'J(IC,ICC)'] == (1, 10, 37, 66, 202, 63, 272, 417, 33, 194, 413, 409, 1260)
_cache[b'J(ICC,IC)'] == _cache[b'J(IC,ICC)']

_cache[b'J(C,IC)'] == _cache[b'J(IC,C)'] == _cache[b'CCIC']
_cache[b'J(CCC,IC)'] == _cache[b'J(IC,CCC)'] == _cache[b'CCCCIC']


_cache[b'P(C,IC)'] == (1, 8, 12)
_cache[b'P(C,CC)'] == (1, 6, 9)
_cache[b'P(ICC,IC)'] == _cache[b'P(IC,ICC)']



from linhomy.data import j_factors_from_ic

def do_j_factors(ic_word):
    # TODO: Refactor to produce more easily checked output.
    return list(j_factors_from_ic(ic_word))

do_j_factors(b'') == []
do_j_factors(b'C') == [(b'', b'')]
do_j_factors(b'CC') == [(b'', b'C'), (b'C', b'')]
do_j_factors(b'CCC') == [(b'', b'CC'), (b'C', b'C'), (b'CC', b'')]
do_j_factors(b'CCI') == [(b'', b'CI'), (b'C', b'I')]
do_j_factors(b'CIC') == [(b'', b'IC')]
