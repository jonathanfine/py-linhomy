from linhomy.structure import Structure

s = Structure({}, {})

s.g_from_CD(0).shape == (1, 1)
s.g_from_CD(1).shape == (1, 1)
s.g_from_CD(2).shape == (2, 2)
s.g_from_CD(3).shape == (3, 3)
s.g_from_CD(4).shape == (5, 5)
s.g_from_CD(5).shape == (8, 8)
