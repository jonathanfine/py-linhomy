import numpy

from linhomy.cdrules import g_from_CD_factory
from linhomy.constants import FIB
from linhomy.constants import FIBWORDS

from linhomy.issue16 import c_rule
from linhomy.issue16 import d_rule

from linhomy.matrices import _cache
from linhomy.matrices import G_matrices

g_matrices = G_matrices(g_from_CD_factory(c_rule, d_rule))

g_from_F = g_matrices.g_from_F
CD_from_g = g_matrices.CD_from_g
g_from_CD = g_matrices.g_from_CD


def str_vec(vec):
    return ''.join(map('{0:x}'.format, vec))


# Find the errors.
errors = []
for n in range(11):
    for v in sorted(set(_cache.values())):
        if len(v) == FIB[n + 1]:
            g_vec = numpy.dot(g_from_F[n], v)
            for i, g in enumerate(g_vec):
                if g < 0:
                    errors.append((n, g_vec, i, g))

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
