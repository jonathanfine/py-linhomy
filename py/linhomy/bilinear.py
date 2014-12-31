import numpy
from .constants import FIB
from .constants import FIBWORDS
from .issue4tools import fib_zeros_array
from .matrices import CD_from_IC
from .matrices import IC_from_CD
from .matrices import J_from_IC


def _J_from_CD(n, m):

    value = fib_zeros_array(n, m, n + m + 1)
    matrix = J_from_IC[n, m]
    rows = numpy.reshape(matrix, (FIB[n+1] * FIB[m+1], -1))

    for i, v in enumerate(FIBWORDS[n]):
        for j, w in enumerate(FIBWORDS[m]):

            coefficients = [
                r * s
                for r in IC_from_CD[n][i]
                for s in IC_from_CD[m][j]
            ]

            join_ic = sum(
                c * r
                for (c, r) in zip(coefficients, rows)
            )

            join_cd = numpy.dot(CD_from_IC[n+m+1], join_ic)
            value[i, j, :] = join_cd

    return value


J_from_CD = dict(
    ((n, m),  _J_from_CD(n, m))
    for n in range(11)
    for m in range(11 - n - 1)
)
