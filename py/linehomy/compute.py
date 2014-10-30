from .fibsubset import Word
from .constants import FIBWORDS


def cd_g_ones(n):
    '''Yield (i,j) for the '1' entries in the CD to g matrix.

    This is with respect to the FIBWORD basis, with each word
    reversed.
    '''

    shapes = tuple(
        # TODO: Hide the intermediate worm.
        Word(w).worm.shape
        for w in FIBWORDS[n]
    )

    for i, a in enumerate(shapes):
        for j, b in enumerate(shapes):
            if a.contains2(b):
                yield i, j

    words = FIBWORDS[n]
