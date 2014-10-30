## 1.  Fibonacci numbers
from linehomy.constants import FIB

# FIB is the Fibonacci numbers.
a = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
FIB[5] == a[5]

# It is a self extending sequence.
len(FIB) == 6
FIB[10] == a[10]
len(FIB) == 11

# TODO: Demonstrate the reset propery (not yet implemented).


## 2. Fibonacci words
from linehomy.constants import FIBWORDS

# Each item is a tuple of bytes using only 1 and 2.
FIBWORDS[0] == (b'',)
FIBWORDS[1] == (b'\x01',)
FIBWORDS[2] == (b'\x01\x01', b'\x02')
FIBWORDS[3] == (b'\x01\x01\x01', b'\x01\x02', b'\x02\x01')

# Each word in FIBWORDS[n] sums to n.
for i in range(10):
    for w in FIBWORDS[i]:
        sum(w) == i

# The sum property for words implies the off-by-one gotcha here.
for i in range(10):
    len(FIBWORDS[i]) == FIB[i+1]

# TODO: Would like to write FIBWORDS[:10].
for i in range(10):
    sorted(FIBWORDS[i]) == list(FIBWORDS[i])

# FIBWORDS[n] is first FIBWORDS[n-1] prefixed with 1.
FIBWORDS[4][:3] == (b'\x01\x01\x01\x01', b'\x01\x01\x02', b'\x01\x02\x01')

# FIBWORDS[n] is then FIBWORDS[n-2] prefixed with 2.
FIBWORDS[4][3:] == (b'\x02\x01\x01', b'\x02\x02')


## 3. CD_G_ONES, the CD to g matrix
from linehomy.constants import CD_G_ONES

# TODO: Same test code on constant.py and compute.py.
CD_G_ONES[1] == [
    (0, 0),
]

CD_G_ONES[2] == [
    (0, 0),
    (1, 1),
]

CD_G_ONES[3] == [
    (0, 0),
    (1, 1), (1, 2),
    (2, 2)
]

CD_G_ONES[4] == [
    (0, 0),
    (1, 1), (1, 2), (1, 3),
    (2, 2),
    (3, 3),
    (4, 4)
]

CD_G_ONES[5] == [
    (0, 0),
    (1, 1), (1, 2), (1, 3), (1, 5),
    (2, 2),
    (3, 3),
    (4, 4), (4, 6), (4, 7),
    (5, 5),
    (6, 6),
    (7, 7)
]
