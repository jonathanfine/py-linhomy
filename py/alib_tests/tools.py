# Self-extending list
from linehomy.tools import MyList

FIB = MyList([0,1])

FIB[0] == 0
FIB[1] == 1
FIB[2] == 1
FIB[3] == 2
FIB[10] == 55

type(FIB) == MyList
type(FIB + [1, 2, 3]) == list
