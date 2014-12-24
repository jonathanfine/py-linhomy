import os
from linhomy.data import _DATAPATH

_DATAPATH.endswith('linhomy/_data') == True
os.path.abspath(_DATAPATH) == _DATAPATH
