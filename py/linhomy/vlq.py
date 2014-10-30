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


# Non-greedy search for a delimiting character.
lex_re = re.compile(b'.*?[\x80-\xff]')


# TODO: Introduce other forms of lex?
def lex(data, pos=0, endpos=sys.maxsize):

    # TODO: How about trailing material?
    # TODO: How about initial non-terminal zero?
    # TODO: What if there isn't a match at all?

    for mo in lex_re.finditer(data, pos, endpos):
        yield mo.group()
