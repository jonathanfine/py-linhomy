from linhomy.issue26 import compose_3

list(compose_3(-1)) == []

list(compose_3(0)) == [
    (0, 0, 0),
    ]

list(compose_3(1)) == [
    (0, 0, 1), (0, 1, 0),
    (1, 0, 0),
    ]

list(compose_3(2)) == [
    (0, 0, 2), (0, 1, 1), (0, 2, 0),
    (1, 0, 1), (1, 1, 0),
    (2, 0, 0),
    ]

list(compose_3(3)) == [
    (0, 0, 3), (0, 1, 2), (0, 2, 1), (0, 3, 0),
    (1, 0, 2), (1, 1, 1), (1, 2, 0),
    (2, 0, 1), (2, 1, 0),
    (3, 0, 0),
]


from linhomy.issue26 import simple_remove
from linhomy.issue26 import slide_remove
from copy import deepcopy
from itertools import count


def do_simple_remove(s, index, n):

    curr = []
    for bit in s.split():
        a, b = bit
        pair = [int(a), int(b)]
        curr.append(pair)

    prev = deepcopy(curr)
    simple_remove(curr, index, n)

    return [
        (i, prev_pair, curr_pair)
        for i, prev_pair, curr_pair in zip(count(), prev, curr)
        if prev_pair != curr_pair
        ]


do_simple_remove('10', 0, 1) == [
    (0, [1, 0], [0, 2])
]
