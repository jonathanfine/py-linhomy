from linhomy.issue28 import iter_deltas


def do_deltas(s):
    size_vec = list(map(int, s))
    return [
       ' '.join(
           ''.join(map(str, pair))
           for pair in item
        )
        for item in  iter_deltas(size_vec)
    ]


# Smoke tests.
do_deltas('') ** ValueError
do_deltas('0') == ['00']
do_deltas('1') == ['00']
do_deltas('2') == ['00']


# Length 2 gives the first non-trivial examples.
do_deltas('00') == ['00 00']

do_deltas('10') == ['00 00', '11 01']
do_deltas('20') == ['00 00', '11 01', '22 02']

do_deltas('01') == ['00 00', '00 12']
do_deltas('02') == ['00 00', '00 12', '00 24']


do_deltas('11') == [
    '00 00', '00 12',
    '11 01', '11 13',
]

do_deltas('12') == [
    '00 00', '00 12', '00 24',
    '11 01', '11 13', '11 25',
]

do_deltas('22') == [
    '00 00', '00 12', '00 24',
    '11 01', '11 13', '11 25',
    '22 02', '22 14', '22 26',
]

from linhomy.issue28 import compose_2

def do_compose_2(n):
    return list(compose_2(n))

do_compose_2(-1) == []
do_compose_2(0) == [(0, 0)]
do_compose_2(1) == [(0, 1), (1, 0)]
do_compose_2(2) == [(0, 2), (1, 1), (2, 0)]
do_compose_2(3) == [(0, 3), (1, 2), (2, 1), (3, 0)]
