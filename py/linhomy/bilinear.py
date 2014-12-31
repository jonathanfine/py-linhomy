import numpy
from .constants import FIB
from .constants import FIBWORDS
from .issue4tools import fib_zeros_array
from .matrices import CD_from_IC
from .matrices import IC_from_CD
from .matrices import J_from_IC


def join_factory(cube, a, b, c):

    n_a, n_b, n_c = cube.shape
    value = numpy.zeros(cube.shape, int)

    matrix = cube
    rows = numpy.reshape(matrix, (n_a * n_b, n_c))

    for i in range(n_a):
        for j in range(n_b):

            coefficients = [
                r * s
                for r in a[i]
                for s in b[j]
            ]

            join_ic = sum(
                c * r
                for (c, r) in zip(coefficients, rows)
            )

            join_cd = numpy.dot(c, join_ic)
            value[i, j, :] = join_cd

    return value


def _J_from_CD(n, m):

    return join_factory(
        J_from_IC[n, m],
        IC_from_CD[n],
        IC_from_CD[m],
        CD_from_IC[n + m + 1]
    )


J_from_CD = dict(
    ((n, m),  _J_from_CD(n, m))
    for n in range(11)
    for m in range(11 - n - 1)
)
