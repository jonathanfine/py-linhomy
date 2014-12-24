import os

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

            data = read_data(J_template, n)

            for line in data.rstrip().split(b'\n'):
                line_key, *rest = line.split()
                self[line_key] = tuple(map(int, rest))

        else:
            raise ValueError

        if key not in self:
            raise ValueError
        else:
            # TODO: Using dict's getitem does not avoid recursion.
            return self[key]


_cache = _Cache()
