'''Produce Fibonacci subsets

Each Fibonacci number counts how many sequences of 1's and 2's there
are with a given sum.  We define the *subordinate* relation, that
associates to each such sequence a subset of other such sequences.
This is used to define the (candidate) formula for linear homology
Betti numbers.
'''

class Word(bytes):

    def __new__(cls, s):

        if isinstance(s, str):
            s = bytes(int(c, 36) for c in s)

        # Check values are in range.
        if s.lstrip(b'\x01\x02'):
            raise ValueError

        return bytes.__new__(cls, s)

    @property
    def mass(self):
        return sum(self)

    @property
    def c(self):
        return self.count(b'\x01')

    @property
    def d(self):
        return self.count(b'\x02')

    def __str__(self):

        if not self:
            return 'Word()'

        format = "Word('{0}')".format
        arg = ''.join(map(str, self))

        return format(arg)

    __repr__ = __str__


# TODO: Refactor this copy and paste based code.
class Worm(bytes):

    def __new__(cls, s):

        mapping = dict()
        mapping['1'] = 1
        mapping['2'] = 2
        mapping['|'] = 3

        lookup = mapping.__getitem__

        if isinstance(s, str):
            s = bytes(map(lookup, s))

            # Already checked that values are in range.
            return bytes.__new__(cls, s)

    @property
    def mass(self):
        return sum(self)

    @property
    def c(self):
        return self.count(b'\x01')

    @property
    def d(self):
        return self.count(b'\x02')

    @property
    def order(self):
        return self.count(b'\x03')


    def __str__(self):

        mapping = dict()
        mapping[1] = '1'
        mapping[2] = '2'
        mapping[3] = '|'
        lookup = mapping.__getitem__

        if not self:
            return "Worm('')"

        format = "Worm('{0}')".format
        arg = ''.join(map(lookup, self))

        return format(arg)

    __repr__ = __str__
