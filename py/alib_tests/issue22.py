from linhomy.issue22 import is_fibword

is_fibword('') == False
is_fibword(b'') == True
is_fibword(b'\x01') == True
is_fibword(b'\x02') == True
is_fibword(b'\x03') == False


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
