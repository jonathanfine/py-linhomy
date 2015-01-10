# Rules is a dict of iterables.
# The iterables produces indexes.
# Each index is bytes, thought of as a sequence of pairs.

# i, j: indices.
# s, t: loop iteration.

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
