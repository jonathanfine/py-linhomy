import collections
import string
from .bytestools import MixIn
from .tools import cache_function

c_from_i_62 = (
    string.digits
    + string.ascii_lowercase
    + string.ascii_uppercase
).__getitem__


i_from_c_62 = dict(
    (c_from_i_62(i), i)
    for i in range(62)
).__getitem__



# GOTCHA: MixIn has to come first.
# GOTCHA: I find myself wanting to type Mixin.
class Index(MixIn, bytes):

    # TODO: Why is this not automatically inherited?
    __hash__ = bytes.__hash__

    def data_from_str(s):

        bits = s.split(':')
        data = []
        for bit in bits:

            if bit == '':
                data.extend([0, 0])
            elif len(bit) == 2:
                data.extend(map(i_from_c_62, bit))
            else:
                raise ValueError

        return bytes(data)

    @property
    def arg(self):

        return ':'.join(
            # Drop redundant '00'.
            '' if pair == (0, 0)
            else ''.join(map(c_from_i_62, pair))
            for pair in self.pairs
        )

    def check_data(data):

        if len(data) % 2:
            raise ValueError

        if min(data) < 0:
            raise ValueError

        if max(data) > 62:
            raise ValueError

    @property
    def order(self):
        return len(self) // 2 - 1


    @property
    def mass(self):

        d_count = sum(self[0::2])
        c_count = sum(self[1::2])
        return c_count + 2 * d_count + 3 * self.order


    @property
    def pairs(self):

        iter_data = iter(b'' + self)
        return tuple(zip(iter_data, iter_data))

    @property
    def c(self):

        d_count, c_count = self[0], self[1]
        body = self[2:]
        if d_count == 0:
            prefix = bytes([0, c_count + 1])
        else:
            prefix = bytes([0, 0, d_count - 1, c_count])

        return Index(prefix + body)

    @property
    def d(self):

        d_count, c_count = self[0], self[1]
        body = self[2:]
        prefix = bytes([d_count + 1, c_count])
        return Index(prefix + body)



def c_rule(index):

    value = []
    d_count, c_count = index[0], index[1]
    body = index[2:]

    value.append((d_count, c_count +1))

    # Skipped if d_count is zero.
    for shift in range(d_count):
        # Order increased by one, which absorbs a D.
        d = d_count - 1 - shift
        c = c_count + 2 * shift
        value.append((0, 0, d, c))

    return tuple(
        Index(bytes(item) + body)
        for item in value
    )


def d_rule(index):

    value = []
    d_count, c_count = index[0], index[1]
    template = list(index.pairs)

    tmp = list(index)
    tmp[0] += 1
    value.append(Index(tmp))

    # GOTCHA: I write index[1] here, took ages to find.
    # TODO: Copy-and-paste tests are dangerous - freeze wrong
    # behaviour, give false reassurance.
    if index[0] == 0:           # No leading D's.

        # Skipped if order is zero.
        for i in range(1, index.order + 1):
            tmp = list(index)
            tmp[1] += 1
            tmp[1 + 2*i] += 1
            value.append(Index(tmp))

    return tuple(map(Index, value))


def d_rule_2(index):

    value = []
    d_count, c_count = index[0], index[1]
    template = list(index.pairs)

    tmp = list(index)
    tmp[0] += 1
    value.append(Index(tmp))

    # GOTCHA: I write index[1] here, took ages to find.
    # TODO: Copy-and-paste tests are dangerous - freeze wrong
    # behaviour, give false reassurance.
    if index[0] == 0:           # No leading D's.

        # Skipped if order is zero.
        for i in range(1, index.order + 1):
            tmp = list(index)

            if 1:
                # Here's a collision.
                #        D     C     C       D        D         C
                #   n =  2     3     4       6        8         9
                # ['', '10', '11', ':01', '10:01', '20:01', ':02:01']
                # ['', '10', ':', '01:', '02:01', '12:01', ':02:01']
                # Break it here -------^^ (not needed for n=5)
                if tmp[-1 + 2 * i] > 0:
                    break

                # Have both indices move together.
                tmp[-1 + 2 * i] += 1
            else:
                # Old behaviour has fixed index here.
                tmp[1] += 1

            tmp[1 + 2*i] += 1
            value.append(Index(tmp))

    return tuple(map(Index, value))


def trace(fn, lines):
    '''For tracking history of applying CD rules.
    '''

    value = []

    for line in lines:
        for item in fn(line[-1]):
            value.append(line + [item])

    return value


def cd_trace_factory(c_rule, d_rule):

    @cache_function
    def cd_trace(cache, n):

        value = {}
        if n >= 1:

            # GOTCHA: It's a dict, cache[-1] means something else.
            for key, lines in cache[n-1].items():
                value[key.c] = trace(c_rule, lines)

            if n >= 2:
                for key, lines in cache[n-2].items():
                    value[key.d] = trace(d_rule, lines)

            return value

        if n == 0:
            return {
                Index(''): [[Index('')]]
            }

    return cd_trace

cd_trace = cd_trace_factory(c_rule, d_rule)


def index_from_fibword(fibword):
    '''Convert fibword into index.

    To bridge the two conventions.
    '''
    # Don't want whole module to depend on .fibsubset
    from .fibsubset import Word

    shape = Word(fibword).worm.shape
    return Index(bytes(reversed(shape)))


def detect_collisions(trace):

    collisions = dict()

    for key, val in trace.items():

        store = collections.defaultdict(list)
        for line in val:
            sub_key = line[-1]
            store[sub_key].append(line)

        for sub_key, lines in store.items():

            if len(lines) >= 2:
                collisions[key, sub_key] = lines

    return collisions


def args_from_collisions(collisions):

    return dict(
        [
            tuple(k.arg for k in key_pair),
            [
                [ind.arg for ind in line]
                for line in lines
            ]
        ]
        for key_pair, lines in collisions.items()
    )


def g_from_CD_helper(fibword):

    prev = (Index(''),)
    for i in reversed(fibword):
        curr = []
        if i == 1:
            rule = c_rule
        elif i == 2:
            rule = d_rule_2
        else:
            ddt

        for item in prev:
                curr.extend(rule(item))

        prev = curr

    return [b'' + w for w in prev]


def fibword_from_index(data):

    # Present data as iterable of pairs.
    # TODO: This could be refactored.
    if len(data) % 2:
        raise ValueError
    iter_data = iter(data)
    pairs = zip(iter_data, iter_data)

    return b'\x01\x02'.join(
        b'\x02' * i + b'\x01' * j
        for i, j in pairs
    )
