## 1. Use of Self-extending list
from linehomy.tools import self_extending_list

@self_extending_list([0, 1])
def FIB(self, key):
    '''The Fibonacci numbers 0, 1, 1, 2, 3, 5, 13, ...

    F(n) = F(n-1) + F(n-2) with F(0) = 1 and F(1) = 1.
    https://oeis.org/A000045
    '''
    return [self[-1] + self[-2]]

FIB[0] == 0
FIB[1] == 1
FIB[2] == 1
FIB[3] == 2
FIB[10] == 55


## 2. Internal properties
from linehomy.tools import SelfExtendingList
type(FIB) == SelfExtendingList
type(FIB + [1, 2, 3]) == list

# TODO: Support slice access.
list(range(7)[0:6:2]) == [0, 2, 4]
FIB[0:6:2] ** TypeError

# TODO: Prevent mutation.
import operator
operator.setitem([0, 1, 2], 1, 2) == None
operator.setitem((0, 1, 2), 1, 2) ** TypeError
operator.setitem(FIB, 1, 2) == None # Should be TypeError
# Tests for del FIB[n].
# Tests for slice assignment and deletion.
# TODO: User MappingProxyType?  New in Python 3.3.
# TODO: truncation, to reclaim memory.
