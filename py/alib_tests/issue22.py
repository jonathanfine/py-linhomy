from linhomy.issue22 import is_word

is_word('') == False
is_word(b'') == True
is_word(b'\x01') == True
is_word(b'\x02') == True
is_word(b'\x03') == False


from linhomy.issue22 import is_index

is_index('') == False
is_index(b'') == False
is_index(b'\x00') == False
is_index(b'\x00\x00') == True
is_index(b'\x00\x05') == True
is_index(b'\x06\x00') == True
is_index(b'\x07\x08') == True
is_index(b'\x07\x08' * 5) == True
is_index(b'\x07\x08\x09' * 5) == False


from linhomy.issue22 import iter_pairs

list(iter_pairs('')) == []
list(iter_pairs('a')) == []
list(iter_pairs('ab')) == [('a', 'b')]
list(iter_pairs('abc')) == [('a', 'b')]
list(iter_pairs('abcd')) == [('a', 'b'), ('c', 'd')]


from linhomy.issue22 import word_from_index

def do_word_from_index(s):

    i = bytes(map(int, s))
    w = word_from_index(i)
    return ''.join(map(str, w))

do_word_from_index('') == ''
do_word_from_index('00') == ''
do_word_from_index('01') == '1'
do_word_from_index('10') == '2'

do_word_from_index('0000') == '12'

do_word_from_index('0200') == '1112'
do_word_from_index('2000') == '2212'
do_word_from_index('2200') == '221112'

do_word_from_index('0002') == '1211'
do_word_from_index('0020') == '1222'
do_word_from_index('0022') == '122211'


from linhomy.issue22 import index_from_word
from linhomy.constants import FIBWORDS


for n in range(10):
    for w in FIBWORDS[n]:
        i = index_from_word(w)
        is_index(i) == True
        w_2 = word_from_index(i)
        is_word(w_2) == True
        w_2 == w


from linhomy.issue22 import _split

def do_split(s):
    return list(_split(s))

do_split('') == [('', '')]
do_split('ab') == [('', 'ab'), ('ab', '')]
do_split('abcd') == [('', 'abcd'), ('ab', 'cd'), ('abcd', '')]


from linhomy.issue22 import iter_lookup

def do_iter_lookup(s, **kwargs):
    rules = dict(
        (k, v.split())
        for k, v in kwargs.items()
    )
    return ' '.join(iter_lookup(rules, s))

do_iter_lookup('') == ''
do_iter_lookup('aa', aa='AA AB') == 'AA AB'
do_iter_lookup('aabb', aa='AA AB') == 'AAbb ABbb'
do_iter_lookup('aabb', aabb='AABB AABb') == 'AABB AABb'
do_iter_lookup('aabb', aa='AA AB', aabb='AABB AABb') == 'AAbb ABbb AABB AABb'
