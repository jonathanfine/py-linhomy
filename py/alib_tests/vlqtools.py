import linhomy.vlqtools as tools

# http://en.wikipedia.org/wiki/Variable-length_quantity


# 1. Lexing a stream of bytes

def doit(src):
    expected = src.split(b' ')
    arg = b''.join(expected)
    actual = list(tools.lex(arg))
    return actual, expected

for src in [
    b'\x80',
    b'\xFF',
    b'aaa\x80 bbb\x81',
]:
    actual, expected = doit(src)
    actual == expected

# GOTCHA:  Need parentheses on RHS.
doit(b'') == ([], [b''])        # TODO: This should fail.


# 2. Convert an int into bytes

from linhomy.vlqtools import cont
from linhomy.vlqtools import term
from linhomy.vlqtools import v_from_u
from linhomy.vlqtools import u_from_v
from linhomy.vlqtools import v_from_s
from linhomy.vlqtools import s_from_v


v_from_u(0) == term(0)
v_from_u(127) == term(127)
v_from_u(128) == cont(1) + term(0)
v_from_u(255) == cont(1) + term(127)
v_from_u(2 ** 14 - 1) == cont(127) + term(127)
v_from_u(2 ** 21- 1) == cont(127) * 2 + term(127)


v_from_s(0) == term(0)
v_from_s(1) == term(2)
v_from_s(2) == term(4)

v_from_s(-1) == term(1)
v_from_s(-2) == term(3)
v_from_s(-3) == term(5)


# TODO: In alib find way to make this a single test?
for i in range(256):
    u_from_v(v_from_u(i)) == i


# 3. Signed integers

from linhomy.vlqtools import s_from_u
from linhomy.vlqtools import u_from_s

# TODO: Create a reference test data and reference implementation?

u_from_s(0) == 0
u_from_s(-1) == 1
u_from_s(1) == 2
u_from_s(-2) == 3
u_from_s(2) == 4

s_from_u(0) == 0
s_from_u(1) == -1
s_from_u(2) == 1

for i in range(10):
    u_from_s(s_from_u(i)) == i

for i in range(-10, 10):
    s_from_u(u_from_s(i)) == i


# 4. Strings

from linhomy.vlqtools import a_from_v
from linhomy.vlqtools import v_from_a

v_from_a('') ** ValueError

v_from_a('A') == term(ord('A'))
v_from_a('Hi') == cont(ord('H')) + term(ord('i'))


for a in [
    'a',
    'ab',
    '\x00',
    '\x7f',
]:
    a_from_v(v_from_a(a)) == a


#5. Pack and unpack

from linhomy.vlqtools import pack
from linhomy.vlqtools import unpack
from linhomy.vlqtools import lex

# TODO: Tests for lex.
# TODO: Tests pass but interface is confusing.

pack('ASU', []) == b''
pack('ASU', [['hi', -4, 3]]) == b'h\xe9\x87\x83'

list(unpack(
    'ASU',
    lex(b'h\xe9\x87\x83'),
)) == [('hi', -4, 3)]

list(unpack(
    'ASU',
    lex(
        b'h\xe9\x87\x83'
        + b'H\xef\x8f\x93'
    ),
)) == [
    ('hi', -4, 3),
    ('Ho', -8, 19),
]
