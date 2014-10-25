## Step 1. Basic words
from linehomy.fibsubset import Word

Word('?') ** ValueError
Word('3') ** ValueError

Word('12').c == 1
Word('12').d == 1
Word('12').mass == 3
str(Word('12')) == repr(Word('12')) == "Word('12')"


## Step 2. Basic worms
from linehomy.fibsubset import Worm

Worm('')
str(Worm('12|')) == repr(Worm('12|')) == "Worm('12|')"

worm = Worm('122|||')
worm.c == 1
worm.d == 2
worm.order == 3
worm.mass == 1 * worm.c + 2 * worm.d + 3 * worm.order == 1 + 4 + 9
del worm

(Word('') == Worm('')) ** TypeError
Worm('') == Worm('')
