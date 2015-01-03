from .cdrules import g_from_CD_factory
from .cdrules import c_rule
from .cdrules import Index

def d_rule(index):

    value = []

    # The easy D-rule.
    tmp = list(index)
    tmp[0] += 1
    value.append(Index(tmp))

    # First case of hard D-rule.
    tmp = list(index)
    if tmp[:4] == [0, 0, 0, 0]:
        prefix = [0, 1, 0, 1]
        value.append(Index(prefix + tmp[4:]))

    # Second case of hard D-rule.
    tmp = list(index)
    if tmp[:6] == [0, 0, 0, 0, 0, 0]:
        prefix = [2, 0, 0, 1]
        value.append(Index(prefix + tmp[6:]))

    # Third case of hard D-rule.
    tmp = list(index)
    if tmp[:6] == [0, 0, 0, 0, 0, 1]:
        prefix = [2, 0, 0, 2]
        value.append(Index(prefix + tmp[6:]))

    # Case four of hard D-rule - [10][74] -> [10][83].
    tmp = list(index)
    if tmp[:6] == [0, 0, 1, 0, 0, 0]:
        prefix = [2, 0, 1, 1]
        value.append(Index(prefix + tmp[6:]))

    # Case five of hard D-rule - [10][64] -> [10][79].
    tmp = list(index)
    if tmp[:6] == [0, 1, 0, 1, 0, 0]:
        prefix = [2, 1, 0, 2]
        value.append(Index(prefix + tmp[6:]))

    return tuple(map(Index, value))

    # Previous code left here for reference.

    # GOTCHA: I write index[1] here, took ages to find.
    # TODO: Copy-and-paste tests are dangerous - freeze wrong
    # behaviour, give false reassurance.
    if index[0] == 0:           # No leading D's.

        # Skipped if order is zero.
        for i in range(1, index.order + 1):
            tmp = list(index)

            if 1:
                # Here's a collision.
                #        D     C     C       D        D         C
                #   n =  2     3     4       6        8         9
                # ['', '10', '11', ':01', '10:01', '20:01', ':02:01']
                # ['', '10', ':', '01:', '02:01', '12:01', ':02:01']
                # Break it here -------^^ (not needed for n=5)
                if tmp[-1 + 2 * i] > 0:
                    break

                # Have both indices move together.
                tmp[-1 + 2 * i] += 1
            else:
                # Old behaviour has fixed index here.
                tmp[1] += 1

            tmp[1 + 2*i] += 1
            value.append(Index(tmp))

    return tuple(map(Index, value))
