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

    if len(index) >= 4:

        tmp[0] = 0              # d_count.
        tmp[1] += d_count + 1
        tmp[3] += d_count + 1

        value.append(Index(tmp))

    return tuple(map(Index, value))
