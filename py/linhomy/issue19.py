from .constants import FIBWORDS

def h_from_g_helper(word):

    i = (word + b'\x01\x02').find(b'\x01\x02')
    pre, post = word[:i], word[i:]

    c, d = pre.count(b'\x01'), pre.count(b'\x02')
    if b'\x02' * d + b'\x01' * c != pre:
        ddt

    for j in range(c//2 + 1):

        # GOTCHA: 2j is complex number.
        new_pre = b'\x02' * (d + j)  + b'\x01' * (c - 2*j)
        yield new_pre + post
