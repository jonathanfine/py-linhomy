import os
from .constants import FIBWORDS

_DATAPATH = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        '_data'
    )
)

IC_template = 'IC-{0}-flag.txt'
J_template = 'J-{0}-flag.txt'


def read_data(template, *argv):

    key = template.format(*argv)
    filename = os.path.join(_DATAPATH, key)
    with open(filename, 'rb') as f:
        return f.read()


def j_twiddle(key):

    if not (key.startswith(b'J(') and key.endswith(b')')):
        raise ValueError

    pre, middle, post = key[:2], key[2:-1], key[-1:]

    i, j = middle.split(b',')

    return pre + j + b',' + i + post

def replace_12_CIC(word):

    return word.replace(b'\x01', b'C').replace(b'\x02', b'IC')


def j_factors_from_ic(ic_word):

    # Removing leading 'C', if possible, for the 'J'.
    if not ic_word.startswith(b'C'):
        return
    ic_tail = ic_word[1:]

    # For as long as possible write as multi-cone.
    for i, c in enumerate(ic_tail):

        yield ic_tail[:i], ic_tail[i:]
        # GOTCHA: c in ic_tail is int.
        if c != ord('C'):
            return

    # Still here?  Nothing but 'C' in tail, so extra item.
    yield ic_tail, b''


class _Cache(dict):
    __slots__ = ()

    def __missing__(self, key):

        # Content of IC-0-flag.txt is unusual.
        if key == b'':
            self[key] = (1,)

        elif set(key).issubset(set(b'CI')):
            data = read_data(IC_template, len(key))

            for line in data.rstrip().split(b'\n'):
                line_key, *rest = line.split()
                self[line_key] = tuple(map(int, rest))

        elif set(key).issubset(set(b'CIJ(),')):

            n = len(key) - 3

            for word in FIBWORDS[n]:
                ic_word = replace_12_CIC(word)
                for i, j in j_factors_from_ic(ic_word):

                    item_key = b'J(' + i + b',' + j + b')'

                    self[item_key] = self[ic_word]
                    self[j_twiddle(item_key)] = self[ic_word]


            data = read_data(J_template, n)

            for line in data.rstrip().split(b'\n'):

                # Needed for when the data is empty.
                if not line:
                    continue

                line_key, *rest = line.split()
                self[line_key] = tuple(map(int, rest))
                self[j_twiddle(line_key)] = self[line_key]

        else:
            raise ValueError

        if key not in self:
            raise ValueError
        else:
            # TODO: Using dict's getitem does not avoid recursion.
            return self[key]


_cache = _Cache()
