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
from functools import partial


def do_mutate(fn, s, index, n):

    curr = []
    for bit in s.split():
        a, b = bit
        pair = [int(a), int(b)]
        curr.append(pair)

    prev = deepcopy(curr)
    fn(curr, index, n)

    return [
        (i, prev_pair, curr_pair)
        for i, prev_pair, curr_pair in zip(count(), prev, curr)
        if prev_pair != curr_pair
        ]


do_simple_remove = partial(do_mutate, simple_remove)
do_slide_remove = partial(do_mutate, slide_remove)

# Out of bounds index but no exception because no removal.
do_simple_remove('', 10, 0) == []
do_slide_remove('', 10, 0) == []

# Here removal so do get exception.
do_simple_remove('', 10, 1) ** IndexError
do_slide_remove('', 10, 1) ** IndexError


# Here is the basic behaviour.  The functions are linear.
do_simple_remove('10', 0, 1) == [
    (0, [1, 0], [0, 2]),
]
do_slide_remove('10 00', 0, 1) == [
    (0, [1, 0], [0, 1]),
    (1, [0, 0], [0, 1]),
]

# Out of bounds exception from slide_remove.
do_slide_remove('10', 0, 1) ** IndexError

# Test linearity.
do_simple_remove('52', 0, 4) == [
    (0, [5, 2], [1, 10]),
]
do_slide_remove('52 67', 0, 4) == [
    (0, [5, 2], [1, 6]),
    (1, [6, 7], [6, 11]),
]

# Test linearity and  change of index.
do_simple_remove('12 34 56 52', 3, 4) == [
    (3, [5, 2], [1, 10]),
]
do_slide_remove('12 34 56 52 67', 3, 4) == [
    (3, [5, 2], [1, 6]),
    (4, [6, 7], [6, 11]),
]


from linhomy.issue26 import make_removal_argv

# Length 0 and 1 are special cases.
make_removal_argv([]) == []
make_removal_argv([3]) == [(0, 0)]


# Test first and last pairs.
make_removal_argv([3, 0]) == [
    ((0, 0), (0, 1), (0, 2), (0, 3)), # First pair.
    ((0, 0),),                        # Last pair.
]

make_removal_argv([0, 3]) == [
    ((0, 0),),                        # First pair.
    ((0, 0), (1, 0), (2, 0), (3, 0)), # Last pair.
]

make_removal_argv([2, 3]) == [
    ((0, 0), (0, 1), (0, 2)),         # First pair.
    ((0, 0), (1, 0), (2, 0), (3, 0)), # Last pair.
]

# Adding to body does not change first or last pairs.
make_removal_argv([3, 4, 5])[0] == make_removal_argv([3, 5])[0]
make_removal_argv([3, 4, 5])[-1] == make_removal_argv([3, 5])[-1]

# Here's a body calculation.
make_removal_argv([2, 4, 2])[1] == (
    (0, 0), (0, 1), (0, 2), (0, 3), (0, 4),
    (1, 0), (1, 1), (1, 2), (1, 3),
    (2, 0), (2, 1), (2, 2),
    (3, 0), (3, 1),
    (4, 0),
)

# Test for all locations in a longer body.
make_removal_argv([2, 4, 2])[1] \
    == make_removal_argv([0, 4, 0])[1] \
    == make_removal_argv([0, 4, 0, 0])[1] \
    == make_removal_argv([0, 0, 4, 0])[2] \
