from functools import partial
import numpy
from linhomy.bilinear import join_factory
from linhomy.bilinear import join_factory_1


cube = numpy.array(range(1, 2*3*1 + 1), int)
cube.shape = 2, 3, 1


def doit(fn, i, j, k, l):

    ell = l                     # Avoid confusion with 1.
    a = numpy.zeros((2, 2), int)
    b = numpy.zeros((3, 3), int)
    c = numpy.eye(1, dtype=int)

    a[i, j] = b[k, ell] = 1

    value = fn(cube, a, b, c)
    value.shape = 2 * 3 * 1
    return list(value)


# Document much of present behaviour of join.

doit_1 = partial(doit, join_factory_1)

doit_1(0, 0, 0, 0) == [1, 0, 0, 0, 0, 0]
doit_1(0, 1, 0, 0) == [4, 0, 0, 0, 0, 0]
doit_1(1, 0, 0, 0) == [0, 0, 0, 1, 0, 0]
doit_1(1, 1, 0, 0) == [0, 0, 0, 4, 0, 0]

doit_1(0, 0, 0, 1) == [2, 0, 0, 0, 0, 0]
doit_1(0, 1, 0, 1) == [5, 0, 0, 0, 0, 0]
doit_1(1, 0, 0, 1) == [0, 0, 0, 2, 0, 0]
doit_1(1, 1, 0, 1) == [0, 0, 0, 5, 0, 0]

doit_1(0, 0, 1, 0) == [0, 1, 0, 0, 0, 0]
doit_1(0, 1, 1, 0) == [0, 4, 0, 0, 0, 0]
doit_1(1, 0, 1, 0) == [0, 0, 0, 0, 1, 0]
doit_1(1, 1, 1, 0) == [0, 0, 0, 0, 4, 0]

doit_1(0, 0, 1, 1) == [0, 2, 0, 0, 0, 0]
doit_1(0, 1, 1, 1) == [0, 5, 0, 0, 0, 0]
doit_1(1, 0, 1, 1) == [0, 0, 0, 0, 2, 0]
doit_1(1, 1, 1, 1) == [0, 0, 0, 0, 5, 0]


# Document desired behaviour of join.

doit = partial(doit, join_factory)

# The j and l values determine where the value is non-zero.
doit(0, 0, 0, 0) == [1, 0, 0, 0, 0, 0]
doit(0, 0, 0, 1) == [0, 1, 0, 0, 0, 0]
doit(0, 0, 0, 2) == [0, 0, 1, 0, 0, 0]

doit(0, 1, 0, 0) == [0, 0, 0, 1, 0, 0]
doit(0, 1, 0, 1) == [0, 0, 0, 0, 1, 0]
doit(0, 1, 0, 2) == [0, 0, 0, 0, 0, 1]

# The i and k values determine what the non-zero value is.
doit(0, 0, 0, 0) == [1, 0, 0, 0, 0, 0]
doit(0, 0, 1, 0) == [2, 0, 0, 0, 0, 0]
doit(0, 0, 2, 0) == [3, 0, 0, 0, 0, 0]

doit(1, 0, 0, 0) == [4, 0, 0, 0, 0, 0]
doit(1, 0, 1, 0) == [5, 0, 0, 0, 0, 0]
doit(1, 0, 2, 0) == [6, 0, 0, 0, 0, 0]

# Here are some mixed tests.
doit(1, 0, 0, 1) == [0, 4, 0, 0, 0, 0]
doit(1, 0, 1, 1) == [0, 5, 0, 0, 0, 0]
doit(1, 1, 0, 0) == [0, 0, 0, 4, 0, 0]
doit(1, 1, 1, 0) == [0, 0, 0, 5, 0, 0]
