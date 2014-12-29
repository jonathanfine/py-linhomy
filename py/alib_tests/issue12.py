from linhomy.cdrules import g_from_CD_helper

# Empty operator.
g_from_CD_helper(b'') == [b'\x00\x00']

# C and D operators.
g_from_CD_helper(b'\x01') == [b'\x00\x01']
g_from_CD_helper(b'\x02') == [b'\x01\x00']

# CD and CD operators.
g_from_CD_helper(b'\x02\x01') == [b'\x01\x01']
g_from_CD_helper(b'\x01\x02') == [b'\x01\x01', b'\x00\x00\x00\x00']

# Hard C, with extra term.
g_from_CD_helper(b'\x01\x02\x02') == [b'\x02\x01', b'\x00\x00\x01\x00', b'\x00\x00\x00\x02']

# Hard D, with extra term.
g_from_CD_helper(b'\x02\x01\x02') == [b'\x02\x01', b'\x01\x00\x00\x00', b'\x00\x01\x00\x01']


from linhomy.cdrules import fibword_from_index

fibword_from_index(b'\x00\x00') == b''

fibword_from_index(b'\x00\x01') == b'\x01'
fibword_from_index(b'\x00\x02') == b'\x01\x01'

fibword_from_index(b'\x01\x00') == b'\x02'
fibword_from_index(b'\x02\x00') == b'\x02\x02'

fibword_from_index(b'\x01\x01') == b'\x02\x01'
fibword_from_index(b'\x02\x01') == b'\x02\x02\x01'
fibword_from_index(b'\x01\x02') == b'\x02\x01\x01'

fibword_from_index(b'\x00\x00\x00\x00') == b'\x01\x02'
fibword_from_index(b'\x00\x00\x01\x02') == b'\x01\x02\x02\x01\x01'
fibword_from_index(b'\x01\x02\x00\x00') == b'\x02\x01\x01\x01\x02'
