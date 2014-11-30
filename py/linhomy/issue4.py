from .constants import FIB
from .constants import FIBWORDS
import numpy as np
from .fibsubset import Word

from .issue4tools import CD_G, G_CD, C_CD, C_G, D_CD, D_G

N = 6                           # Was 12.

def wibble(s):

    return Word(s).worm.shape.arg


def doit_C(n):
    print('C in the g basis.')
    m = n + 1

    for j in range(FIB[n+1]):
        for i in range(FIB[m+1]):

            coeff = C_G[m][i, j]
            if coeff:

                i_str = wibble(FIBWORDS[m][i])
                j_str = wibble(FIBWORDS[n][j])

                coeff = '{0:+}'.format(coeff)
                print(coeff, j_str, i_str)

    print()


def doit_D(n):

    m = n + 2
    print('''D in the g basis - n = ''' + str(n))

    for j in range(FIB[n+1]):
        for i in range(FIB[m+1]):
            coeff = D_G[m][i, j]
            if coeff:

                i_str = wibble(FIBWORDS[m][i])
                j_str = wibble(FIBWORDS[n][j])

                print(coeff, j_str, i_str)

    print()


if __name__ == '__main__':

    for i in range(N-1):
        doit_C(i)

    for n in range(0, N-2):
        doit_D(n)
