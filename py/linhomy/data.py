import os

_DATAPATH = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        '_data'
    )
)


def read_data(template, *argv):

    key = template.format(*argv)
    filename = os.path.join(_DATAPATH, key)
    with open(filename, 'rb') as f:
        return f.read()
