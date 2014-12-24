import os
from linhomy.data import _DATAPATH

_DATAPATH.endswith('linhomy/_data') == True
os.path.abspath(_DATAPATH) == _DATAPATH


from linhomy.data import read_data

# This is fairly regular.
read_data('IC-{0}-flag.txt', 0) == b'p 1\n'
read_data('IC-{0}-flag.txt', 1) == b'C 1\n'
read_data('IC-{0}-flag.txt', 2) == b'CC 1 3\nIC 1 4\n'


# This is odd.  Skipping join where one factor is 'C' * n.
# Also a couple of missing files?
# TODO: How to import FileNotFoundError, which is real exception?
read_data('J-{0}-flag.txt', 0) ** OSError
read_data('J-{0}-flag.txt', 1) ** OSError
read_data('J-{0}-flag.txt', 2) == b''
read_data('J-{0}-flag.txt', 3) == b''
read_data('J-{0}-flag.txt', 4) == b''
read_data('J-{0}-flag.txt', 5) == b'J(IC,IC) 1 8 24 34 104 24 104 160\n'
