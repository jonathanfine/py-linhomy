# Rules is a dict of iterables.
# The iterables produces indexes.
# Each index is bytes, thought of as a sequence of pairs.

# c, d: number of C's and D's.
# i, j: indices.
# s, t: loop iteration.
# v, w: words


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


# TODO: Refactor and add iter_tuples.
def iter_pairs(items):
    '''Yield (item[0], item[1]), (item[2], item[3]), etc.

    The items need only be an iterable.  Does not check that number of
    items is even.
    '''

    iter_items = iter(items)
    return zip(iter_items, iter_items)


def word_from_index(i):
    '''Return word that corresponds to index i.

    Does not check that i is an index.
    '''

    # Present data as iterable of pairs.
    # TODO: This could be refactored.
    iter_data = iter(i)
    pairs = zip(iter_data, iter_data)

    return b'\x01\x02'.join(
        b'\x02' * d + b'\x01' * c
        for d, c in iter_pairs(i)
    )


def index_from_word(w):
    '''Return index that corresponds to word w.

    Does not check that w is a word.
    '''

    # First deal with troublesome special case.
    if w == b'':
        return b'\x00\x00'

    pending = []
    for bit in w.split(b'\x01\x02'):
        c = bit.count(b'\x01')
        d = bit.count(b'\x02')
        pending.extend([d, c])

    return bytes(pending)



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
