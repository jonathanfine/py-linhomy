'''Produce Fibonacci subsets

Each Fibonacci number counts how many sequences of 1's and 2's there
are with a given sum.  We define the *subordinate* relation, that
associates to each such sequence a subset of other such sequences.
This is used to define the (candidate) formula for linear homology
Betti numbers.
'''

import itertools
from .bytestools import MixIn

class ThisCannotHappen(Exception):
    pass

class Word(MixIn, bytes):

    @staticmethod
    def data_from_str(s):

        if isinstance(s, str):
            data = bytes(int(c, 36) for c in s)
        return data


    @staticmethod
    def check_data(data):

        # Check values are in range.
        if data.lstrip(b'\x01\x02'):
            raise ValueError


    @property
    def arg(self):
        '''Return object that can be passed to constructor.'''
        return ''.join(map(str, self))


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
    def worm(self):

        data = self.replace(b'\x02\x01', b'\x03')
        return Worm(data)



class Worm(MixIn, bytes):

    @staticmethod
    def data_from_str(s):

        mapping = dict()
        mapping['1'] = 1
        mapping['2'] = 2
        mapping['|'] = 3

        lookup = mapping.__getitem__

        return bytes(map(lookup, s))


    @staticmethod
    def check_data(data):

        # Check values are in range.
        if data.lstrip(b'\x01\x02\x03'):
            raise ValueError

    @property
    def arg(self):

        mapping = dict()
        mapping[1] = '1'
        mapping[2] = '2'
        mapping[3] = '|'
        lookup = mapping.__getitem__

        return ''.join(map(lookup, self))


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


    @property
    def word(self):

        data = self.replace(b'\x03', b'\x02\x01')
        return Word(data)

    @property
    def shape(self):

        # Deal with troublesome special case.
        if False and not self:
            # TODO: Gotcha - want to write Shape('') or Shape().
            return Shape(';00')

        bits = self.split(b'\x03')

        pending = []
        for bit in bits:
            c = bit.count(b'\x01')
            d = bit.count(b'\x02')
            pending.extend([c, d])

        data = bytes(pending)
        return Shape(data)


class Shape(MixIn, bytes):

    @staticmethod
    def data_from_str(s):

        # TODO: Replace by base36.
        def doit(chars):
            c, d = chars
            return int(c), int(d)

        body_str, tail_str = s.split(';')

        # Process the body_str.
        int_data = []
        if body_str:            # Shape(';00').
            for seg in body_str.split(','):
                int_data.extend(doit(seg))

        # Process the tail_str.
        int_data.extend(doit(tail_str))

        return bytes(int_data)


    @staticmethod
    def check_data(data):

        length = len(data)
        if length % 2 or length < 2:
            raise ValueError

    @property
    def arg(self):

        shape_format = '{0};{1}'.format
        segment_format = '{0}{1}'.format

        # Split into body and tail.  Assume length is even.
        body, tail = self[:-2], self[-2:]

        # Create body_str.
        iter_body = iter(body)
        body_str = ','.join(
            segment_format(*seg)
            for seg
            in zip(iter_body, iter_body)
        )

        # Create tail_str.
        tail_str = segment_format(*tail)

        return shape_format(body_str, tail_str)


    @property
    def order(self):
        return len(self) // 2 - 1


    @property
    def mass(self):

        c_mass = sum(self[::2])
        d_mass = sum(self[1::2])

        return c_mass + 2 * d_mass + 3 * self.order


    def expand_data(self, delimiter):

        # Split into body and tail.  Assume length is even.
        body, tail = self[:-2], self[-2:]

        # Process the body.
        iter_body = iter(body)
        for c, d in zip(iter_body, iter_body):
            yield b'\x01' * c
            yield b'\x02' * d
            yield delimiter

        # Process the tail.
        c, d = tail
        yield b'\x01' * c
        yield b'\x02' * d


    @property
    def word(self):

        data = b''.join(self.expand_data(b'\x02\x01'))
        return Word(data)

    @property
    def worm(self):

        data = b''.join(self.expand_data(b'\x03'))
        return Worm(data)


    def contains(self, other):

        value = self._contains(other)
        return value == True


    # TODO: Is this transitive?  I think so.
    def _contains(self, other):
        '''As contains, except returns explanation for False.
        '''

        # Deal with the simple cases first.
        if type(self) != type(other):
            raise TypeError

        # TODO: ValueError?
        if len(self) != len(other):
            return 'Unequal length', len(self), len(other)

        # TODO: ValueError?
        if self.mass != other.mass:
            return 'Unequal mass', self.mass, other.mass


        # Produce list of (c_1, d_1, c_2, d_2) quads.
        iter_1, iter_2  = iter(self), iter(other)
        quads = list(zip(iter_1, iter_1, iter_2, iter_2))

        # Split into body_quads and tail_quad (note tail singular).
        body_quads = quads[:-1]
        tail_quad = quads[-1]

        # The body loop.
        mass_1 = mass_2 = 0
        for i,  (c_1, d_1, c_2, d_2) in enumerate(body_quads):

            # Each other segment to have at least as many d's.
            if not d_1 <= d_2:
                return 'Too little d', i, d_1, d_2

            # Keep a running total of the mass.
            mass_1 += c_1 + 2 * d_1 + 3
            mass_2 += c_2 + 2 * d_2 + 3

            # The other total mass to be no larger than self.
            if not mass_2 <= mass_1:
                return 'Too much mass', i, mass_1, mass_2

        # Now check the tail.
        c_1, d_1, c_2, d_2 = tail_quad

        # The other tail to have at least as many d's.
        if not d_1 <= d_2:
            return 'Too little tail d', d_1, d_2

        # TODO: Clarify this code and logic.
        # Any extra d must come from extra c (and not existing c).
        extra_c, extra_d = c_2 - c_1, d_2 - d_1

        # Consistency check - and to help explain the logic.
        if not mass_1 - mass_2 == extra_c + 2 * extra_d:
            raise ThisCannotHappen

        # TODO: Unpack into two stages.
        # Too much tail d, Tail too short.
        if not (d_2 <= d_1 + c_1 <= c_2 + d_2):
            return 'Too much tail d', extra_d, extra_c

        # Still here?  Then true.
        return True


    def contract(self, indices):

        # Handle special case of no indices.
        if not indices:
            return self

        # Check indices are in bounds.
        indices = set(indices)
        index_list = sorted(indices)

        if not 0 <= index_list[0]:
            raise ValueError('negative index')

        # Ensures loop finishes with pending.extend.
        if not index_list[-1] <= len(self) - 2:
            raise ValueError('nothing to join')

        # The main loop iterates over (i, c, d) triples.
        iter_self = iter(self)
        triples = zip(itertools.count(), iter_self, iter_self)

        # Start the main loop.
        pending = []
        c_total = d_total = 0
        for i, c, d in triples:

            c_total += c
            d_total += d

            if i in indices:
                c_total += 1
                d_total += 1
            else:
                pending.extend([c_total, d_total])
                c_total, d_total = 0, 0

        data = bytes(pending)

        # Check for logic error.
        value = Shape(data)
        if value.mass != self.mass:
            raise ThisCannotHappen

        return value


    # TODO: Rename.
    # TODO: Return value more helpful for testing?
    def _helper(self, other):
        '''Compute where to contract.
        '''
        # Deal with the simple cases first.
        if type(self) != type(other):
            raise TypeError

        # TODO: ValueError?
        if self.mass != other.mass:
            return False

        # Iterate over the d counts.
        other_ds = iter(other[1::2])
        skips = []

        # Iterate over the d counts.
        for i, d_self in enumerate(self[1::2]):

            # TODO: For testing return the new d's?
            d_other = next(other_ds)
            while d_other < d_self:
                # TODO: It's rude to raise StopIteration.
                d_other += next(other_ds)
                d_other += 1
                skips.append(i)

        return skips


    # TODO: Rename?
    def contains2(self, other):

        try:
            indices = self._helper(other)
        except StopIteration:
            return False

        contracted = other.contract(indices)

        return self.contains(contracted)
