import numpy

from linhomy.cdrules import g_from_CD_factory
from linhomy.constants import FIB
from linhomy.constants import FIBWORDS

from linhomy.issue16 import c_rule
from linhomy.issue16 import d_rule

from linhomy.matrices import _cache
from linhomy.matrices import G_matrices

MAX = 6                         # Make run quicker.
g_matrices = G_matrices(g_from_CD_factory(c_rule, d_rule), max=MAX)

g_from_F = g_matrices.g_from_F
CD_from_g = g_matrices.CD_from_g
g_from_CD = g_matrices.g_from_CD


def str_vec(vec):
    return ''.join(map('{0:x}'.format, vec))


# Find the errors.
errors = []
for n in range(MAX + 1):
    for v in sorted(set(_cache.values())):
        if len(v) == FIB[n + 1]:
            g_vec = numpy.dot(g_from_F[n], v)
            for i, g in enumerate(g_vec):
                if g < 0:
                    errors.append((n, g_vec, i, g))

# This is resolved by adding second case of hard D-rule.
if 0:
    len(errors) == 30

    # Report first error.
    errors[0][0] == 8
    n, g_vec, i, g = errors[0]
    cd_vec = numpy.dot(CD_from_g[n], g_vec)
    row_vec = g_from_CD[n][i,:]

    # The problem we have to fix.
    str_vec(g_vec) == '1252053256020530002003441043232-110'
    str_vec(cd_vec) == '1200013-100000000000000100013-1-1-1000'
    str_vec(row_vec) == '0000000000000000000000000000001100'


    # Pointers to how to fix the problem.
    [
        j for (j, c) in enumerate(cd_vec)
        if c > 0
    ] == [0, 1, 5, 6, 22, 26, 27]
    FIBWORDS[n][i] == b'\x02\x02\x01\x02\x01'
    FIBWORDS[n][27] == b'\x02\x01\x02\x01\x02'


# This is resolved by adding third case of hard D-rule.
if 0:
    len(errors) == 18

    # Report first remaining error.
    errors[0][0] == 9
    n, g_vec, i, g = errors[0]
    cd_vec = numpy.dot(CD_from_g[n], g_vec)
    row_vec = g_from_CD[n][i,:]

    # The problem we have to fix.
    str_vec(g_vec) == '12420321531205320020053100000200003441022143120320-10100'
    str_vec(cd_vec) == '1200002-1110000000000000000000000000100002-111000-1-1000000'
    str_vec(row_vec) == '0000000000000000000000000000000000000000000000001111000'


    # Pointers to how to fix the problem.
    [
        j for (j, c) in enumerate(cd_vec)
        if c > 0
    ] == [0, 1, 6, 8, 9, 35, 40, 42, 43]
    FIBWORDS[n][i] == b'\x02\x02\x01\x02\x01\x01'

    # Two candidates.  Which do we choose?
    FIBWORDS[n][40] == b'\x02\x01\x01\x02\x01\x02'
    FIBWORDS[n][43] == b'\x02\x01\x02\x01\x01\x02'
    # I chose this one
    # '\x02\x01\x02\x01\x01\x02'
    #                      ^^^^
    # The trailing \x02 is moved to the front.
    # '\x02\x02\x01\x02\x01\x01'
    #  ^^^^

    # This one is too long, I think.
    FIBWORDS[n][42] == b'\x02\x01\x02\x01\x01\x01\x01'


# The remaining errors are now more complicated.  Need to think about this.
# Some of these are fixed by rules four and five
if 0:

    g_vecs = [item[1] for item in errors]
    cd_vecs = [numpy.dot(CD_from_g[n], g_vec) for g_vec in g_vecs]

    list(map(str_vec, g_vecs)) == [
        # Look carefully - there are now three columns that contains
        # negative values.  Previously there was on one such column
        # (for a given n).  This might indicate that something else is
        # going wrong.
        '124203213201053110200531200002000053110000000002000000034420221220104311020032000-10010000',
        '1122020052320523002005230000020000523000000000020000000324101004232042300200312-10-10010000',
        '1122020052320523002005230000020000523000000000020000000324101004232042300200312-10-10010000',
        '112204114101052120200521400002000052120000000002000000032230311310104212020031010-10010000',
        '112202003121051310200513200002000051310000000002000000032420100212104131020031200-10010000',
        '102202004011050320200503400002000050320000000002000000030430100301104032020030210-10010000',
        '111202002000051130200511600002000051130000000002000000032240100100004113020031120-10010000',
        # These two rows are the same - that's odd - maybe something is wrong here.
        '1244152252020b5362712b53c400071020b5362000000007100020045672221220108536261264231-30-141010',
        '1244152252020b5362712b53c400071020b5362000000007100020045672221220108536261264231-30-141010',
    ]


    # Pointers to how to fix the problem.

    # Negative components in the g vectors.
    negatives = [
        [(i, c) for (i, c) in enumerate(g_vec) if c < 0]
        for g_vec in g_vecs
    ]

    negatives == [
        [(81, -1)],
        [(79, -1), (81, -1)],
        [(79, -1), (81, -1)],
        [(81, -1)],
        [(81, -1)],
        [(81, -1)],
        [(81, -1)],
        [(81, -3), (83, -1)],
        [(81, -3), (83, -1)],
     ]

    sum(map(len, negatives)) == 13
    len(errors) == len(negatives) == 9

    # The index (actually fibword) for the negative indices.
    FIBWORDS[10][79] == b'\x02\x02\x01\x01\x02\x01\x01'
    FIBWORDS[10][81] == b'\x02\x02\x01\x02\x01\x01\x01'
    FIBWORDS[10][83] == b'\x02\x02\x01\x02\x02\x01'

    # Interesting positive components in the cd vectors.
    [
        [(i, c) for (i, c) in enumerate(cd_vec) if c > 0 and i > 25]
        for cd_vec in cd_vecs
    ] == [
        [(56, 1), (61, 2), (68, 1), (69, 1)],
        [(57, 1), (63, 1), (64, 2), (65, 1)], # (79, -1).
        [(57, 1), (63, 1), (64, 2), (65, 1)], # (79, -1).
        [(58, 1), (60, 1), (61, 1), (69, 1), (71, 1)],
        [(56, 1), (64, 1), (65, 1), (68, 1), (70, 1)],
        [(57, 1), (63, 1), (65, 1), (70, 2)],
        [(56, 1), (68, 1), (69, 1), (71, 2)],
        [(56, 1), (61, 2), (68, 1), (69, 2), (71, 2), (72, 2), (74, 1)], # (83, -1).
        [(56, 1), (61, 2), (68, 1), (69, 2), (71, 2), (72, 2), (74, 1)], # (83, -1).
     ]

    def rot(w):
        return w[1:] + w[:1]

    FIBWORDS[10][56] == b'\x02\x01\x01\x01\x01\x01\x01\x02'
    FIBWORDS[10][57] == b'\x02\x01\x01\x01\x01\x01\x02\x01'
    FIBWORDS[10][58] == b'\x02\x01\x01\x01\x01\x02\x01\x01'
    FIBWORDS[10][60] == b'\x02\x01\x01\x01\x02\x01\x01\x01'
    FIBWORDS[10][63] == b'\x02\x01\x01\x02\x01\x01\x01\x01'
    FIBWORDS[10][68] == b'\x02\x01\x02\x01\x01\x01\x01\x01'

    FIBWORDS[10][61] == b'\x02\x01\x01\x01\x02\x01\x02'
    FIBWORDS[10][64] == b'\x02\x01\x01\x02\x01\x01\x02' == rot(FIBWORDS[10][79])
    FIBWORDS[10][65] == b'\x02\x01\x01\x02\x01\x02\x01'
    FIBWORDS[10][69] == b'\x02\x01\x02\x01\x01\x01\x02'
    FIBWORDS[10][70] == b'\x02\x01\x02\x01\x01\x02\x01'
    FIBWORDS[10][71] == b'\x02\x01\x02\x01\x02\x01\x01'

    FIBWORDS[10][72] == b'\x02\x01\x02\x01\x02\x02'
    FIBWORDS[10][74] == b'\x02\x01\x02\x02\x01\x02' == rot(FIBWORDS[10][83])


####################################
if MAX >= 10:

    g_vecs = [item[1] for item in errors]
    cd_vecs = [numpy.dot(CD_from_g[n], g_vec) for g_vec in g_vecs]

    list(map(str_vec, g_vecs)) == [
        # Now just one column of negatives.
        '124203213201053110200531200002000053110000000002000000034420221220104311020032020-10010000',
        '112202005232052300200523000002000052300000000002000000032410100423204230020031210-10010000',
        '112204114101052120200521400002000052120000000002000000032230311310104212020031020-10010000',
        '112202003121051310200513200002000051310000000002000000032420100212104131020031210-10010000',
        '102202004011050320200503400002000050320000000002000000030430100301104032020030210-10010000',
        '111202002000051130200511600002000051130000000002000000032240100100004113020031120-10010000',
        '1244152252020b5362712b53c400071020b5362000000007100020045672221220108536261264251-30041010',
    ]


    # Pointers to how to fix the problem.

    # Negative components in the g vectors.
    negatives = [
        [(i, c) for (i, c) in enumerate(g_vec) if c < 0]
        for g_vec in g_vecs
    ]

    negatives == [
        [(81, -1)],
        [(81, -1)],
        [(81, -1)],
        [(81, -1)],
        [(81, -1)],
        [(81, -1)],
        [(81, -3)],
    ]

    sum(map(len, negatives)) == 7
    len(errors) == len(negatives) == 7

    # The index (actually fibword) for the negative indices.
    FIBWORDS[10][81] == b'\x02\x02\x01\x02\x01\x01\x01'

    # Interesting positive components in the cd vectors.
    [
        [(i, c) for (i, c) in enumerate(cd_vec) if c > 0 and i > 25]
        for cd_vec in cd_vecs
    ] == [

        [(56, 1), (61, 2), (68, 1), (69, 1)], # [10][69].
        [(57, 1), (63, 1), (64, 2), (65, 1)],
        [(58, 1), (60, 1), (61, 1), (69, 1), (71, 1)], # [10][69].
        [(56, 1), (64, 1), (65, 1), (68, 1), (70, 1)],
        [(57, 1), (63, 1), (65, 1), (70, 2)],
        [(56, 1), (68, 1), (69, 1), (71, 2)], # [10][69].
        [(56, 1), (61, 2), (68, 1), (69, 2), (71, 2), (72, 2), (74, 1)], # [10][69].
     ]

    def rot(w):
        return w[1:] + w[:1]

    # This goes part way towards solving the problem.
    FIBWORDS[10][69] == b'\x02\x01\x02\x01\x01\x01\x02' == rot(FIBWORDS[10][81])
