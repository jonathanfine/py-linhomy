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


def v_from_u(uint):

    # TODO: Docstring.

    if uint < 0:
        raise ValueError

    # This is worth special casing.
    if uint < 128:
        # GOTCHA: list of ints.
        return term(uint)

    pending = []
    while uint > 0:

        uint, remainder = divmod(uint, 128)
        pending.append(remainder)

    # VLQ is bigendian so least significant byte terminates.
    pending[0] += 128

    # VLQ is bigendian so need reverse iteration on pending.
    return bytes(reversed(pending))


def v_from_s(sint):

    return v_from_u(u_from_s(sint))


def u_from_v(vlq):

    uint = 0
    for b in vlq:
        uint = uint * 128 + (b & 127)

    return uint


def s_from_v(vlq):

    return s_from_u(u_from_v(vlq))


def s_from_u(uint):

    if uint < 0:
        raise ValueError

    value, neg = divmod(uint, 2)

    if neg:
        # 1 --> (0, 1) --> -1.
        # 3 --> (1, 1) --> -2.
        return -value -1
    else:
        # 0 --> (0, 0) --> 0.
        # 2 --> (1, 0) --> 1.
        return value


def u_from_s(sint):

    if sint >= 0:
        # 0 --> 0.
        # 2 --> 1.
        return 2 * sint
    else:
        # Here, sint is negative, -sint positive.
        # -1 --> 2 --> 1.
        # -2 --> 4 --> 3.
        return -2 * sint  - 1


def v_from_a(ascii):

    if ascii == '':
        raise ValueError

    # Create list of uints, lying between 0 and 127.
    uints = list(map(ord, ascii))
    if not max(uints) < 128:
        raise ValueError

    uints[-1] += 128            # Set the terminal indicator.
    return bytes(uints)


def a_from_v(vlq):

    uints = list(vlq)
    uints[-1] -= 128            # Clear the terminal indicator.
    return ''.join(map(chr, uints))
