import linhomy.vlq as vlq

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
