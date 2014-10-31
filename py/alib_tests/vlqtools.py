import linhomy.vlqtools as vlq

# http://en.wikipedia.org/wiki/Variable-length_quantity


# 1. Lexing a stream of bytes

def doit(src):
    expected = src.split(b' ')
    arg = b''.join(expected)
    actual = list(vlq.lex(arg))
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

bfi = vlq.bytes_from_int
cont, term = vlq.cont, vlq.term

bfi(0) == term(0)
bfi(127) == term(127)
bfi(128) == cont(1) + term(0)
bfi(255) == cont(1) + term(127)
bfi(2 ** 14 - 1) == cont(127) + term(127)
bfi(2 ** 21- 1) == cont(127) * 2 + term(127)

# TODO: In alib find way to make this a single test?
for i in range(256):
    vlq.uint_from_vlq(bfi(i)) == i


# 3. Signed integers
s_from_lsb = vlq.sint_from_lsbint
lsb_from_s = vlq.lsbint_from_sint

# TODO: Create a reference test data and reference implementation?
lsb_from_s(0) == 0
lsb_from_s(-1) == 1
lsb_from_s(1) == 2
lsb_from_s(-2) == 3
lsb_from_s(2) == 4

s_from_lsb(0) == 0
s_from_lsb(1) == -1
s_from_lsb(2) == 1

for i in range(10):
    lsb_from_s(s_from_lsb(i)) == i

for i in range(-10, 10):
    s_from_lsb(lsb_from_s(i)) == i
