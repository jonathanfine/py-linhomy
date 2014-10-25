'''Produce Fibonacci subsets

Each Fibonacci number counts how many sequences of 1's and 2's there
are with a given sum.  We define the *subordinate* relation, that
associates to each such sequence a subset of other such sequences.
This is used to define the (candidate) formula for linear homology
Betti numbers.
'''

from .bytestools import MixIn

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
