## Step 1. Basic words
from linhomy.fibsubset import Word
from linhomy.fibsubset import ThisCannotHappen

Word('?') ** ValueError
Word('3') ** ValueError

Word('12').c == 1
Word('12').d == 1
Word('12').mass == 3
str(Word('12')) == repr(Word('12')) == "Word('12')"


## Step 2. Basic worms
from linhomy.fibsubset import Worm

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
from linhomy.fibsubset import Shape

# Length must be even number, at least two.
Shape(b'') ** ValueError
Shape(b'\x00') ** ValueError
Shape(b'\x00\x01\x02') ** ValueError

# This works.
Shape(';00')
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


Shape(';41').mass == Shape(';22').mass == 6


sh1.contains(sh1) == True
Shape(';41').contains(Shape(';22')) == False


# Every worm has a shape.
Worm('').shape == Shape(';00')
Worm('12').shape == Worm('21').shape == Shape(';11')
Worm('12|').shape == Worm('21|').shape == Shape('11;00')


# Step 5. Contraction of a shape
# TODO: More testing.
Shape('12,34;12').contract([0]) == Shape('57;12')
Shape('12,34;12').contract([1]) == Shape('12;57')


# TODO: Return value / exception more helpful for testing?
Shape('12,34;12')._helper(Shape('12;57')) ** StopIteration
Shape('12;57')._helper(Shape('12,34;12')) == [1]


# TODO: Fix? # : need more than 1 value to unpack
Shape('12:57') ** ValueError


# Tests for _contains.
def doit(getter, giver):
    getter = Shape(getter)
    giver = Shape(giver)
    return getter._contains(giver)

# Smoke test.
doit(';00', ';00') == True

# Tail tests.
doit(';00', '00;00') == ('Unequal length', 2, 4)
doit(';10', ';00') == ('Unequal mass', 1, 0)
doit(';01', ';20') == ('Too little tail d', 1, 0)
doit(';20', ';01') == ('Too much tail d', 1, -2)

# Body tests.
doit('01;00', '20;00') == ('Too little d', 0, 1, 0)
doit('00,10;00', '10,00;00') == ('Too much mass', 0, 3, 4)


# Tests for gives and gets.
def gets(getter, giver):
    ''' Return getter gets a contribution from giver.

    Arguments are construction strings for Shape.
    '''
    getter = Shape(getter)
    giver = Shape(giver)
    return getter.contains2(giver)


# Smoke test.
gets(';00', ';00') == True
gets('12,34;12', '12;57') == False
gets('12;57', '12,34;12') == True

# Intersection homology - n = 4, g_1.
gets(';31', ';31') == True
gets(';31', '00;20') == True
gets(';31', '10;10') == True
gets(';31', '20;00') == True

# Linear homology - n = 5 - CDCC / g_{1121}.
gets('20;00', '20;00') == True
gets('20;00', '10;10') == False # Should be True.
gets('20;00', '00;20') == False # Should be True.
gets('20;00', '01;00') == False # Should be True.


doit('20;00', '10;10') == True

# TODO: Puzzle - explain
gets('20;00', '10;10') == False # Should be True.
