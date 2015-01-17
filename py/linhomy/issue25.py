from .cdrules import Index

def c_rule(index):

    value = []
    d_count, c_count = index[0], index[1]
    body = index[2:]

    value.append((d_count, c_count +1))

    # Skipped if d_count is zero.
    for shift in range(d_count):
        # Order increased by one, which absorbs a D.
        d = d_count - 1 - shift
        c = c_count + 2 * shift
        value.append((0, 0, d, c))

    return tuple(
        Index(bytes(item) + body)
        for item in value
    )


def d_rule(index):

    value = []
    d_count, c_count = index[0], index[1]
    template = list(index.pairs)

    tmp = list(index)
    tmp[0] += 1
    value.append(Index(tmp))

    # GOTCHA: I write index[1] here, took ages to find.
    # TODO: Copy-and-paste tests are dangerous - freeze wrong
    # behaviour, give false reassurance.
    if index[0] == 0:           # No leading D's.

        # Skipped if order is zero.
        for i in range(1, index.order + 1):
            tmp = list(index)
            tmp[1] += 1
            tmp[1 + 2*i] += 1
            value.append(Index(tmp))

    return tuple(map(Index, value))
