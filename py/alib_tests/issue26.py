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
make_removal_argv([3]) == [((0, 0),)]


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


from linhomy.issue26 import iter_remove

def do_remove(s):

    # Copied from do_mutate.
    pairs = []
    for bit in s.split():
        a, b = bit
        pair = [int(a), int(b)]
        pairs.append(pair)

    value = []
    for item in iter_remove(pairs):

        tmp = ' '.join(
            ''.join(map(str, pair))
            for pair in item
        )

        value.append(tmp)

    return value


# Smoke tests.
# TODO: Use colons in the input string notation.
do_remove('00') == ['00']
do_remove('00 00') == ['00 00']
do_remove('00 00 00') == ['00 00 00']

do_remove('45') == ['45']
do_remove('03 05') == ['03 05']

# Just first or last.
do_remove('30 00') == ['30 00', '21 01', '12 02', '03 03']
do_remove('00 30') == ['00 30', '00 22', '00 14', '00 06']

# Both first and last.
do_remove('20 20') == [
    '20 20', '20 12', '20 04',
    '11 21', '11 13', '11 05',
    '02 22', '02 14', '02 06',
]

# An example of body.
do_remove('00 30 00') == [
    '00 30 00', '00 21 01', '00 12 02', '00 03 03',
    '00 22 00', '00 13 01', '00 04 02',
    '00 14 00', '00 05 01',
    '00 06 00',
]

# Size is 3 x 6 x 3 = 54.
do_remove('20 20 20') == [

    # Prefix '20'.
    '20 20 20', '20 20 12', '20 20 04',
    '20 11 21', '20 11 13', '20 11 05',
    '20 02 22', '20 02 14', '20 02 06',

    '20 12 20', '20 12 12', '20 12 04',
    '20 03 21', '20 03 13', '20 03 05',

    '20 04 20', '20 04 12', '20 04 04',

    # Prefix '11'
    '11 21 20', '11 21 12', '11 21 04',
    '11 12 21', '11 12 13', '11 12 05',
    '11 03 22', '11 03 14', '11 03 06',

    '11 13 20', '11 13 12', '11 13 04',
    '11 04 21', '11 04 13', '11 04 05',

    '11 05 20', '11 05 12', '11 05 04',

    # Prefix '02'.
    '02 22 20', '02 22 12', '02 22 04',
    '02 13 21', '02 13 13', '02 13 05',
    '02 04 22', '02 04 14', '02 04 06',

    '02 14 20', '02 14 12', '02 14 04',
    '02 05 21', '02 05 13', '02 05 05',

    '02 06 20', '02 06 12', '02 06 04'
]

# Put them in order - destroys any clear pattern.
sorted(do_remove('20 20 20')) == [
    '02 04 06', '02 04 14', '02 04 22', '02 05 05', '02 05 13', '02 05 21',
    '02 06 04', '02 06 12', '02 06 20', '02 13 05', '02 13 13', '02 13 21',
    '02 14 04', '02 14 12', '02 14 20', '02 22 04', '02 22 12', '02 22 20',
    '11 03 06', '11 03 14', '11 03 22', '11 04 05', '11 04 13', '11 04 21',
    '11 05 04', '11 05 12', '11 05 20', '11 12 05', '11 12 13', '11 12 21',
    '11 13 04', '11 13 12', '11 13 20', '11 21 04', '11 21 12', '11 21 20',
    '20 02 06', '20 02 14', '20 02 22', '20 03 05', '20 03 13', '20 03 21',
    '20 04 04', '20 04 12', '20 04 20', '20 11 05', '20 11 13', '20 11 21',
    '20 12 04', '20 12 12', '20 12 20', '20 20 04', '20 20 12', '20 20 20'
]

# No duplicates (and exactly 54).
len(do_remove('20 20 20')) == len(set(do_remove('20 20 20'))) == 54
