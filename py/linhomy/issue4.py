from .constants import FIB
from .constants import FIBWORDS
import numpy as np
from .fibsubset import Word

from .issue4tools import CD_G, G_CD, C_CD, C_G, D_CD, D_G

N = 12

def doit_C(n):
    print('C in the g basis.')
    m = n + 1
    # Start with something in the G basis.
    curr = G_CD[n]                  # Now in CD basis.
    curr = np.dot(C_CD[n], curr)    # Bump dimension.
    curr = np.dot(CD_G[m], curr)    # Now in G basis.

    if 0:
        print(curr)
        print()

    for j in range(FIB[n+1]):
        for i in range(FIB[m+1]):
            sgn = curr[i, j]
            if sgn:
                i_str = ''.join(str(k) for k in FIBWORDS[m][i])
                j_str = ''.join(str(k) for k in FIBWORDS[n][j])

                j_str = Word(j_str).worm.shape.arg
                i_str = Word(i_str).worm.shape.arg

                sgn = '{0:+}'.format(sgn)
                print(sgn, j_str, i_str)

    print()


def doit_D(n):

    m = n + 2
    print('''D in the g basis - n = ''' + str(n))
    curr = G_CD[n]                  # Now in CD basis.
    curr = np.dot(D_CD[n], curr)    # Bump dimension.
    curr = np.dot(CD_G[m], curr)    # Now in G basis.

    if 0:
        print(curr)

    for j in range(FIB[n+1]):
        for i in range(FIB[m+1]):
            coeff = curr[i, j]
            if coeff:
                # GOTCHA: Off by one error here.
                i_str = ''.join(str(k) for k in FIBWORDS[m][i])
                j_str = ''.join(str(k) for k in FIBWORDS[n][j])

                if 0:
                    print(i, j, j_str, i_str)

                i_str = Word(i_str).worm.shape.arg
                j_str = Word(j_str).worm.shape.arg
                print(coeff, j_str, i_str)

    print()


if __name__ == '__main__':

    for i in range(N-1):
        doit_C(i)

    for n in range(0, N-2):
        doit_D(n)
