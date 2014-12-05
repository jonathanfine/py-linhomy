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

    if index[1] == 0:

        # Skipped if order is zero.
        for i in range(1, index.order + 1):
            tmp = list(index)
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


@cache_function
def cd_trace(cache, n):

    value = {}
    if n >= 1:

        # GOTCHA: It's a dict, cache[-1] means something else.
        for key, lines in cache[n-1].items():
            value['C' + key] = trace(c_rule, lines)

        if n >= 2:
            for key, lines in cache[n-2].items():
                value['D' + key] = trace(d_rule, lines)

        return value

    if n == 0:
        return {
            '': [[Index('')]]
        }
