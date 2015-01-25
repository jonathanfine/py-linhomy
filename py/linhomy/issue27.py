import itertools
from .cdrules import index_from_fibword
from .issue26 import iter_contribute


def g_from_CD_0(fibword):

    # According to matrices.py, _g_from_CD passes a fibword to
    # supplied g_from_CD (as coded here), and expects an iterable of
    # indexes, i.e. pairs.

    # The simple thing that does not fall over is
    #   return [b'' + index_from_fibword(fibword)]

    return [b'' + index_from_fibword(fibword)]


def g_from_CD_1(fibword):

    # Convert fibword in pairs, list of pairs of integers.
    index = index_from_fibword(fibword)
    iter_index = iter(index)
    pairs = list(zip(iter_index, iter_index))

    # Contributions is iterable of pairs of integers.
    contributions = iter_contribute(pairs)

    value = []
    for contrib in contributions:
        b = bytes(itertools.chain(*contrib))
        value.append(b)

    return value
