import numpy

from linhomy.cdrules import g_from_CD_factory
from linhomy.constants import FIB

from linhomy.issue16 import c_rule
from linhomy.issue16 import d_rule_2

from linhomy.matrices import _cache
from linhomy.matrices import G_matrices

g_matrices = G_matrices(g_from_CD_factory(c_rule, d_rule_2))

g_from_F = g_matrices.g_from_F


# Find the errors.
errors = []
for n in range(11):
    for v in sorted(set(_cache.values())):
        if len(v) == FIB[n + 1]:
            g_vec = numpy.dot(g_from_F[n], v)
            for i, g in enumerate(g_vec):
                if g < 0:
                    errors.append((n, g_vec, i, g))

len(errors) == 29

# Report first error.
errors[0][0] == 8
''.join(map('{0:x}'.format, errors[0][1])) == '1252053296040533002003440043232-110'
