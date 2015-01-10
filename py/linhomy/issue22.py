# Rules is a dict of iterables.
# The iterables produces indexes.
# Each index is bytes, thought of as a sequence of pairs.

# i, j: indices.
# s, t: loop iteration.


def is_fibword(b):
    '''Return True if type(b) is bytes, all in 1 and 2.
    '''
    return (
        type(b) == bytes
        # GOTCHA: If b is bytes then set(b) is ints.
        and set(b).issubset({1, 2})
    )


def is_index(b):
    '''Return True if type(b) is bytes, length in 2, 4, 6, 8, etc.
    '''
    return (
        type(b) == bytes
        and not len(b) % 2
        and len(b) >= 2
    )


def _split(i):

    n = len(i)
    if n % 2:
        raise ValueError
    for s in range(0, n + 1, 2):
        yield i[:s], i[s:]


def iter_lookup(rules, i):
    '''Iterate over result of applying rule to index i.'''

    for pre, post in _split(i):
        for new_pre in rules.get(pre, ()):
            yield new_pre + post
