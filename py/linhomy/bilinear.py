import numpy

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
