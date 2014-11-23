from linhomy.constants import CD_G_ONES
from linhomy.constants import FIBWORDS

EXPECT_5 = [
    ('11111', '11111'),
    ('1112', '1112 1121 1211 2111'),
    ('122','122 212 221'),
    ('1121', '1121 1211 2111 221'),
    ('1211', '1211 2111 212'),
    ('2111', '2111'),
    ('221', '221'),
    ('212', '212'),
]


expect = set()
for getter, givers in EXPECT_5:
    for giver in givers.split():
        expect.add((getter, giver))


actual = set()
for getter, giver in CD_G_ONES[5]:

    getter = ''.join(str(i) for i in FIBWORDS[5][getter])
    giver = ''.join(str(i) for i in FIBWORDS[5][giver])

    actual.add((getter, giver))


sorted(expect.difference(actual)) == [] # Missing 1's.
sorted(actual.difference(expect)) == [] # Extra 1's.
