import itertools
from .cdrules import fibword_from_index
from .cdrules import index_from_fibword
from .constants import FIBWORDS
from .issue4tools import fib_zeros_array


def g_from_CD_0(fibword):

    # According to matrices.py, _g_from_CD passes a fibword to
    # supplied g_from_CD (as coded here), and expects an iterable of
    # indexes, i.e. pairs.

    # The simple thing that does not fall over is
    #   return [b'' + index_from_fibword(fibword)]

    return [b'' + index_from_fibword(fibword)]



def pairs_from_fibword(fibword):

    # Convert fibword in pairs, list of pairs of integers.
    fibword = bytes(reversed(fibword)) # GOTCHA.
    index = index_from_fibword(fibword)
    iter_index = iter(index)
    pairs = list(zip(iter_index, iter_index))
    return pairs


def fibword_from_pairs(pairs):

    b = bytes(itertools.chain(*pairs))
    return fibword_from_index(b)


def g_from_CD_factory(iter_contribute):


    def g_from_CD_matrix(n):
        '''Return numpy g_from_CD matrix, for dimension n.
        '''
        value = fib_zeros_array(n, n)

        # GOTCHA:  We're finding columns.
        for j, v in enumerate(FIBWORDS[n]):
            pairs = pairs_from_fibword(v)
            for contrib in iter_contribute(pairs):
                w = fibword_from_pairs(contrib)
                i = FIBWORDS[n].index(w)
                value[i, j] += 1

        return value

    def g_from_CD(fibword):

        # Convert fibword in pairs, list of pairs of integers.
        fibword = bytes(reversed(fibword)) # GOTCHA.
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


    return g_from_CD_matrix, g_from_CD
