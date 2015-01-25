import functools
from linhomy.issue26 import compose_3

def do_generic(fn, pairs_str):
    '''Wrap fn as a pairs to list of pair function.
    '''
    pairs = []
    for bit in pairs_str.split():
        a, b = bit
        pair = [int(a), int(b)]
        pairs.append(pair)

    # Also copied.
    value = []
    for item in fn(pairs):

        tmp = ' '.join(
            ''.join(map(str, pair))
            for pair in item
        )

        value.append(tmp)

    return value


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

do_remove = functools.partial(do_generic, iter_remove)

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


from linhomy.issue26 import join_at

def do_join_at(s1, s2):

    # Copied from do_mutate.
    pairs = []
    for bit in s1.split():
        a, b = bit
        pair = [int(a), int(b)]
        pairs.append(pair)

    flags = list(map(int, s2))
    value = join_at(pairs, flags)

    return ' '.join(
        ''.join(map(str, pair))
        for pair in value
    )


# Smoke tests.
do_join_at('00', '') == '00'
do_join_at('12', '') == '12'

do_join_at('00', '0') ** ValueError
do_join_at('00 00', '') ** ValueError

# Examples of not joining and joining.
do_join_at('12 34', '0') == '12 34'
do_join_at('12 34', '1') == '57'


from linhomy.issue26 import slide_helper

def do_slide_helper(fixed_str, rest_str):

    fixed = list(map(int, fixed_str))
    rest = list(map(int, rest_str))
    return list(
        ''.join(map(str, item))
        for item in slide_helper(fixed, rest)
    )


# Smoke tests.
do_slide_helper('', '') == ['']
do_slide_helper('', '0') == ['0']
do_slide_helper('', '1') == ['1']
do_slide_helper('', '2') == ['2']

# Smoke tests, with fixed.
do_slide_helper('456', '') == ['456']
do_slide_helper('456', '0') == ['4560']
do_slide_helper('456', '1') == ['4561']
do_slide_helper('456', '2') == ['4562']

# Test sliding.
do_slide_helper('', '30') == ['30', '21', '12', '03']
do_slide_helper('', '31') == ['31', '22', '13', '04']
do_slide_helper('', '32') == ['32', '23', '14', '05']

# Test sliding, with fixed.
do_slide_helper('456', '32') == ['45632', '45623', '45614', '45605']

# Test longer sliding.
do_slide_helper('', '0000') == ['0000']
do_slide_helper('', '1000') == ['1000', '0100', '0010', '0001']

do_slide_helper('', '2000') == [
    '2000',                     # No sliding.
    '1100', '1010', '1001',     # Slide 1 once.
    '0200',                     # Slide 2 once ...
    '0110', '0101',             # ... and then slide.
    '0020',                     # Slide 2 twice ...
    '0011',                     # ... and then slide.
    '0002',                     # Slide 2 thrice.
]

# There's a pattern here.
do_slide_helper('', '1100') == [
    '1100',
    '1010', '1001',
    '0200', '0110', '0101',
    '0020', '0011',
    '0002',
]

# A sample value.
tmp = list(slide_helper([], [4, 3, 2, 1, 0]))

# The items come out in reversed lexicographic order.
tmp == list(reversed(sorted(tmp)))

# The items are all distinct.
for i, j in zip(tmp, tmp[1:]):
    i != j

# This gives all ways of summing to 10 (with 5 parts).
len(list(slide_helper([], [10, 0, 0, 0, 0]))) == 1001

# There's a lot of ways of summing this way to 10.
len(list(slide_helper([], [4, 3, 2, 1, 0]))) == 795

# Not so many this way.
len(list(slide_helper([], [0, 1, 2, 3, 4]))) == 37


from linhomy.issue26 import join_and_slide

do_j_and_s = functools.partial(do_generic, join_and_slide)

# Smoke tests.
do_j_and_s('00') == ['00']
do_j_and_s('00 00') == ['00 00', '11']

# TODO: Preserve reverse lexicographic order?
do_j_and_s('00 00 00') == [
    '00 00 00',                 # Unchanged.
    '00 11',                    # Join at second opportunity.
    '11 00',                    # Join at first opportunity.
    '10 01',                    # Slide.
    '22',                       # Join at both opportunities.
]


from linhomy.issue26 import iter_contribute

do_contribute = functools.partial(do_generic, iter_contribute)

# Smoke tests.
do_contribute('00') == ['00']
do_contribute('01') == ['01']
do_contribute('02') == ['02']

do_contribute('10') == ['10']
do_contribute('20') == ['20']

do_contribute('00 00') == ['00 00', '11']
do_contribute('00 01') == ['00 01', '12']
do_contribute('00 02') == ['00 02', '13']

# n = 5.
do_contribute('00 10') == [
    '00 10',                    # Unchanged.
    '00 02',                    # Simple D rule.
    '21',                       # Join.
]

do_contribute('10 00') == [
    '10 00',                    # Unchanged.
    '01 01',                    # Complex D rule.
    '21',                       # Join.
]

# n = 6.
do_contribute('00 00 00') == [
    '00 00 00',                 # Unchanged.
    '00 11', '00 03',           # Join, and simple D rule.
    '11 00', '02 01',           # Join, and complex D rule.
    '10 01',                    # Slide '11 00'
    '01 02',                    # Complex D rule '10 01'.
    '22',                       # Join both.
]
