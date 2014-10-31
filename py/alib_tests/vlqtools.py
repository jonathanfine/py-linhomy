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


v_from_u(0) == term(0)
v_from_u(127) == term(127)
v_from_u(128) == cont(1) + term(0)
v_from_u(255) == cont(1) + term(127)
v_from_u(2 ** 14 - 1) == cont(127) + term(127)
v_from_u(2 ** 21- 1) == cont(127) * 2 + term(127)

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
