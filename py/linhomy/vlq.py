import re
import sys

# http://en.wikipedia.org/wiki/Variable-length_quantity

# TODO: Is this material needed?
if 0:
    # The first (most significant) bit of the last byte is 1.
    constants = dict(
        MSB_0 = b'[\x00-\x80]',
        MSB_1 = b'[\x80-\xff]',
        ZERO = b'\x00',
    )

    constants.update(
        VLQ = '{MSB_0}+{MSB_1}'.format(**constants)
    )


# Very useful in testing.
def cont(n):
    if not 0 <= n < 128:
        raise ValueError
    return bytes([n])

def term(n):
    if not 0 <= n < 128:
        raise ValueError
    return bytes([n + 128])


# TODO: Perhaps useful.
if 0:
    CONT_ZERO = cont(0)
    TERM_ZERO = term(0)


# Non-greedy search for a delimiting character.
lex_re = re.compile(b'.*?[\x80-\xff]')


# TODO: Introduce other forms of lex?
def lex(data, pos=0, endpos=sys.maxsize):

    # TODO: How about trailing material?
    # TODO: How about initial non-terminal zero?
    # TODO: What if there isn't a match at all?

    for mo in lex_re.finditer(data, pos, endpos):
        yield mo.group()


def bytes_from_int(n):

    # TODO: Docstring.

    if n < 0:
        raise ValueError

    # This is worth special casing.
    if n < 128:
        # GOTCHA: list of ints.
        return bytes([n + 128])

    pending = []
    while n > 0:

        n, remainder = divmod(n, 128)
        pending.append(remainder)

    # VLQ is bigendian so least significant byte terminates.
    pending[0] += 128

    # VLQ is bigendian so need reverse iteration on pending.
    return bytes(reversed(pending))


def uint_from_vlq(vlq):

    value = 0
    for b in vlq:
        value = value * 128 + (b & 127)

    return value
