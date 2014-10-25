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

# Misc

(Word('') == Worm('')) ** TypeError
Worm('') == Worm('')


# Step 3. Worms from words and vice versa
Word('12').worm == Worm('12')
Word('21').worm == Worm('|')

Worm('|').word == Word('21')


# Step 4. Shapes
from linehomy.fibsubset import Shape

# Length must be even number, at least two.
Shape(b'') ** ValueError
Shape(b'\x00') ** ValueError
Shape(b'\x00\x01\x02') ** ValueError

# This works.
sh = Shape(b'\x00\x00')

# TODO: Don't mention tail if 'empty'.
sh.arg == ';00'
str(sh) == "Shape(';00')"

sh1 = Shape(b'\x00\x01\x02\x03\x04\x05')
str(sh1) == "Shape('01,23;45')"
sh1 == Shape('01,23;45')

# Can convert shape to worm and word.
sh1 = Shape('01,23;45')
sh1.worm == Worm('2|11222|111122222')
sh1.word == Word('2211122221111122222')


Shape('00;41').mass == Shape('00;22').mass == 9


sh1.contains(sh1) == True
Shape('00;41').contains(Shape('00;22')) == False

Shape(';00') ** ValueError      # TODO: Fix.
