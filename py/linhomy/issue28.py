def iter_deltas(size_vec):
    '''Yield changes contributed by size_vec.

    '''
    length = len(size_vec)

    if length == 0:
        raise ValueError

    if length == 1:
        yield tuple(size_vec)
