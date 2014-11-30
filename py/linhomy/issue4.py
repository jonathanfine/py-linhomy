from .constants import CD_G_ONES
from .constants import FIB
from .constants import FIBWORDS
import numpy as np
from .fibsubset import Word
from .fibtools import compute

N = 12
CD_G = [None] * N
G_CD = [None] * N
C_CD = [None] * (N - 1)
C_G = [None] * (N - 1)
D_CD = [None] * (N - 2)
D_G = [None] * (N - 2)


for i, j in CD_G_ONES[6]:

    m = 6
    i_str = ''.join(str(k) for k in FIBWORDS[m][i])
    j_str = ''.join(str(k) for k in FIBWORDS[m][j])

    i_str = Word(i_str).worm.shape.arg
    j_str = Word(j_str).worm.shape.arg

    # Display lookup table.
    if 0:
        print(i, j, i_str, j_str)

if 0:
    print(CD_G_ONES[6])


if 1:
    for n in range(N):
        for w in FIBWORDS[n]:
            shape = Word(w).worm.shape
            ones = compute(shape)
            if 0:
                print(list(map(FIBWORDS[n].index, ones)))



for n in range(N):

    shape = (FIB[n+1], FIB[n+1])
    cd_g = np.zeros(shape, int)

    if 1:
        for i, w in enumerate(FIBWORDS[n]):
            # GOTCHA: Can't use shape.
            fib_shape = Word(w).worm.shape
            ones = compute(fib_shape)
            for v in ones:
                j = FIBWORDS[n].index(v)
                cd_g[i, j] = 1

    else:
        for i, j in CD_G_ONES[n]:
            cd_g[i, j] = 1

        if n == 6:
    #        print(cd_g[6,10])
    #        cd_g[6, 10] = 0
            cd_g[2, 10] = 1
            cd_g[4, 10] = 1
            cd_g[5, 10] = 1

    g_cd = np.linalg.inv(cd_g)
    g_cd = np.rint(g_cd, np.zeros(shape, int))
    CD_G[n] = cd_g
    G_CD[n] = g_cd

    if 0:
        print(cd_g)


for n in range(N-1):

    shape = (FIB[n+2], FIB[n+1])

    c_cd = np.zeros(shape, int)
    for j, w in enumerate(FIBWORDS[n]):

        w_2 = w + b'\x01'
        i = FIBWORDS[n+1].index(w_2)

        c_cd[i, j] = 1

    C_CD[n] = c_cd


for n in range(N-2):

    shape = (FIB[n+3], FIB[n+1])

    d_cd = np.zeros(shape, int)
    for j, w in enumerate(FIBWORDS[n]):

        w_2 = w + b'\x02'
        i = FIBWORDS[n+2].index(w_2)

        d_cd[i, j] = 1

    D_CD[n] = d_cd



if 1:
    print('CD to g - n = 5')
    data = CD_G_ONES[5]
    m = np.zeros((8, 8), int)
    for i, j in data:
        m[i,j] = 1
    print(m)
    print()

if 0:
    t = np.zeros((8, 13), int)
    for i, w in enumerate(FIBWORDS[5]):

        w_2 = w + b'\x01'
        j = FIBWORDS[6].index(w_2)
        t[i, j] = 1


def doit(n):
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

for i in range(N-1):
    doit(i)

if 0:
    curr = G_CD[5]                  # Now in CD basis.
    curr = np.dot(C_CD[5], curr)    # Bump dimension.
    curr = np.dot(C_CD[6], curr)    # Bump dimension.
    curr = np.dot(CD_G[7], curr)    # Now in G basis.

    print(curr)

if 0:

    curr = G_CD[5]                  # Now in CD basis.
    curr = np.dot(C_CD[5], curr)    # Bump dimension.
    curr = np.dot(C_CD[6], curr)    # Bump dimension.
    curr = np.dot(C_CD[7], curr)    # Bump dimension.
    curr = np.dot(CD_G[8], curr)    # Now in G basis.

    print(curr)


if 0:
    # Start with something in the CD basis.
    curr = np.eye(8, dtype=int)
    curr = np.dot(C_CD[5], curr)    # Bump dimension.
    curr = np.dot(CD_G[6], curr)    # Now in G basis.

    print(curr)


if 0:
    # Start with something in the CD basis.
    curr = np.eye(8, dtype=int)
    curr = np.dot(C_CD[5], curr)    # Bump dimension.
    curr = np.dot(C_CD[6], curr)    # Bump dimension.
    curr = np.dot(CD_G[7], curr)    # Now in G basis.

    print(curr)

if 0:
    # Start with something in the CD basis.
    curr = np.eye(8, dtype=int)
    curr = np.dot(C_CD[5], curr)    # Bump dimension.
    curr = np.dot(C_CD[6], curr)    # Bump dimension.
    curr = np.dot(C_CD[7], curr)    # Bump dimension.
    curr = np.dot(CD_G[8], curr)    # Now in G basis.

    print(curr)


def doit(n):

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


for n in range(0, N-2):
    doit(n)
