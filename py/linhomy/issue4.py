from .constants import FIB
from .constants import FIBWORDS
import numpy as np
from .fibsubset import Word

from .issue4tools import CD_G, G_CD, C_CD, C_G, D_CD, D_G

N = 6                           # Was 12.

def wibble(s):

    return Word(s).worm.shape.arg


def non_zero_entries(matrix):

    n_fib, m_fib = matrix.shape
    if n_fib == 1 or m_fib == 1:
        raise ValueError

    tmp = [FIB[0]]
    while tmp[-1] < max(n_fib, m_fib):
        tmp.append(FIB[len(tmp)])

    n = tmp.index(n_fib) - 1
    m = tmp.index(m_fib) - 1

    for j in range(m_fib):
        for i in range(n_fib):
            coeff = matrix[i, j]
            if coeff:
                i_word = FIBWORDS[n][i]
                j_word = FIBWORDS[m][j]
                yield j_word, i_word, coeff


def print_entries(entries):

    for j_word, i_word, coeff in entries:

        i_str = wibble(i_word)
        j_str = wibble(j_word)

        coeff = '{0:+}'.format(coeff)
        print(coeff, j_str, i_str)


if __name__ == '__main__':

    for n in range(2, N-1):

        print('C in the g basis.')
        print_entries(non_zero_entries(C_G[n]))
        print()

    for n in range(2, N-2):

        print('''D in the g basis - n = ''' + str(n))
        print_entries(non_zero_entries(D_G[n]))
        print()
