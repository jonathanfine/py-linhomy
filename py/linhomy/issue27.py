from .cdrules import index_from_fibword

def g_from_CD(fibword):

    # According to matrices.py, _g_from_CD passes a fibword to
    # supplied g_from_CD (as coded here), and expects an iterable of
    # indexes, i.e. pairs.

    # The simple thing that does not fall over is
    #   return [b'' + index_from_fibword(fibword)]

    return [b'' + index_from_fibword(fibword)]
