import numpy
from linhomy.bilinear import join_factory


cube = numpy.array(range(1, 2*3*1 + 1), int)
cube.shape = 2, 3, 1


def doit(a_i, a_j, b_i, b_j):

    a = numpy.zeros((2, 2), int)
    b = numpy.zeros((3, 3), int)
    c = numpy.eye(1, dtype=int)

    a[a_i, a_j] = 1
    b[b_i, b_j] = 1

    value = join_factory(cube, a, b, c)
    value.shape = 2 * 3 * 1
    return list(value)


# Document much of the behaviour of join.
doit(0, 0, 0, 0) == [1, 0, 0, 0, 0, 0]
doit(0, 1, 0, 0) == [4, 0, 0, 0, 0, 0]
doit(1, 0, 0, 0) == [0, 0, 0, 1, 0, 0]
doit(1, 1, 0, 0) == [0, 0, 0, 4, 0, 0]

doit(0, 0, 0, 1) == [2, 0, 0, 0, 0, 0]
doit(0, 1, 0, 1) == [5, 0, 0, 0, 0, 0]
doit(1, 0, 0, 1) == [0, 0, 0, 2, 0, 0]
doit(1, 1, 0, 1) == [0, 0, 0, 5, 0, 0]

doit(0, 0, 1, 0) == [0, 1, 0, 0, 0, 0]
doit(0, 1, 1, 0) == [0, 4, 0, 0, 0, 0]
doit(1, 0, 1, 0) == [0, 0, 0, 0, 1, 0]
doit(1, 1, 1, 0) == [0, 0, 0, 0, 4, 0]

doit(0, 0, 1, 1) == [0, 2, 0, 0, 0, 0]
doit(0, 1, 1, 1) == [0, 5, 0, 0, 0, 0]
doit(1, 0, 1, 1) == [0, 0, 0, 0, 2, 0]
doit(1, 1, 1, 1) == [0, 0, 0, 0, 5, 0]
