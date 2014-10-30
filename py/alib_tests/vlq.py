import linhomy.vlq as vlq

# http://en.wikipedia.org/wiki/Variable-length_quantity


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
