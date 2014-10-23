from linehomy.fibsubset import Word

Word('?') ** ValueError
Word('3') ** ValueError

Word('12').c == 1
Word('12').d == 1
Word('12').mass == 3
str(Word('12')) == repr(Word('12')) == "Word('12')"
