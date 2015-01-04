import itertools
import numpy
from .bilinear import join_factory
from .cdrules import fibword_from_index
from .constants import FIB
from .constants import FIBWORDS
from .data import _cache
from .data import replace_12_CIC
from .issue4tools import fib_zeros_array
from .issue4tools import linalg_int_inv


def _F_from_IC(n):

    words = FIBWORDS[n]
    value = fib_zeros_array(n, n)

    for i, w in enumerate(words):
        ic_word = replace_12_CIC(w)
        if 1:
            # The flag vectors of the IC words are the columns.
            value[:,i] = _cache[ic_word]
        else:
            # Previous value.  They are not the rows.
            value[i,:] = _cache[ic_word]

    return value


F_from_IC = [
    _F_from_IC(n)
    for n in range(11)
]

IC_from_F = list(map(linalg_int_inv, F_from_IC))


# IC = D + CC.
def CD_from_IC_helper(cd_word):

    pending = []
    for piece in cd_word.split(b'\x02'):
        if piece:
            pending.append((piece,))

        pending.append((b'\x01\x01', b'\x02'))

    del pending[-1]

    for items in itertools.product(*pending):
        yield b''.join(items)


def _CD_from_IC(n):

    value = fib_zeros_array(n, n)
    words = FIBWORDS[n]

    for i, w in enumerate(words):
        for v in CD_from_IC_helper(w):
            j = words.index(v)
            # Transpose - the v give columns, not rows.
            value[j, i] += 1

    return value


CD_from_IC =  [
    _CD_from_IC(n)
    for n in range(11)
]

IC_from_CD = list(map(linalg_int_inv, CD_from_IC))


CD_from_F = [
    numpy.dot(CD_from_IC[n], IC_from_F[n])
    for n in range(11)
]

F_from_CD = [
    numpy.dot(F_from_IC[n], IC_from_CD[n])
    for n in range(11)
]
# TODO: linalag_int_inv ValueError: list(map(linalg_int_inv, CD_from_F))

def _J_from_IC(n, m):

    value = fib_zeros_array(n, m, n + m + 1)
    for i, v in enumerate(FIBWORDS[n]):
        for j, w in enumerate(FIBWORDS[m]):

            # Prepare to look up flag vector of join.
            v_IC = replace_12_CIC(v)
            w_IC = replace_12_CIC(w)
            join_word = b'J(' + v_IC + b',' + w_IC + b')'

            # Look up join flag vector, convert to IC vector.
            join_flag = _cache[join_word]
            join_ic = numpy.dot(IC_from_F[n+m+1], join_flag)
            value[i, j, :] = join_ic

    return value


J_from_IC = dict(
    ((n, m),  _J_from_IC(n, m))
    for n in range(11)
    for m in range(11 - n - 1)
)


J_from_CD = dict(
    ((n, m),  join_factory(
        J_from_IC[n, m],
        IC_from_CD[n],
        IC_from_CD[m],
        CD_from_IC[m + n + 1]
    ))
    for n in range(11)
    for m in range(11 - n - 1)
)


# TODO: Started as copy of J_from_IC.
# Changes: J -> P, join -> product (mostly), +1 ->, -1 ->.
def _P_from_IC(n, m):

    value = fib_zeros_array(n, m, n + m)
    for i, v in enumerate(FIBWORDS[n]):
        for j, w in enumerate(FIBWORDS[m]):

            # Prepare to look up flag vector of join.
            v_IC = replace_12_CIC(v)
            w_IC = replace_12_CIC(w)
            product_word = b'P(' + v_IC + b',' + w_IC + b')'

            # Look up join flag vector, convert to IC vector.
            product_flag = _cache[product_word]
            product_ic = numpy.dot(IC_from_F[n+m], product_flag)
            value[i, j, :] = product_ic

    return value


P_from_IC = dict(
    ((n, m),  _P_from_IC(n, m))
    for n in range(11)
    for m in range(11 - n)
)


P_from_CD = dict(
    ((n, m),  join_factory(
        P_from_IC[n, m],
        IC_from_CD[n],
        IC_from_CD[m],
        CD_from_IC[m + n]
    ))
    for n in range(11)
    for m in range(11 - n)
)


class G_matrices:
    '''Given g_from_CD_rules compute and store matrices.

    See .cdrules.g_from_CD_helper for format of the rules function.

    '''

    def __init__(self, g_from_CD_rules):

        self.g_from_CD_rules = g_from_CD_rules

        # Compute g_from_CD and CD_from_g.
        self.g_from_CD =  [
            self._g_from_CD(n)
            for n in range(11)
        ]

        self.CD_from_g = list(map(linalg_int_inv, self.g_from_CD))

        # Compute g_from_F and F_from_g.
        self.g_from_F = [
            numpy.dot(self.g_from_CD[n], CD_from_F[n])
            for n in range(11)
        ]

        self.F_from_g = [
            numpy.dot(F_from_CD[n], self.CD_from_g[n])
            for n in range(11)
        ]

        # Can now compute J_from_g.
        self.J_from_g = dict(
            ((n, m),  join_factory(
                # TODO: Note that earlier version have J_from_IC here - BLUNDER.
                J_from_CD[n, m],
                self.CD_from_g[n],
                self.CD_from_g[m],
                self.g_from_CD[m + n + 1]
            ))
            for n in range(11)
            for m in range(11 - n - 1)
        )


    # This helper computes g_from_CD using the supplied rules.
    def _g_from_CD(self, n):

        words = FIBWORDS[n]
        value = fib_zeros_array(n, n)

        # Each word gives a column.
        for j, v in enumerate(words):
            for w_index in self.g_from_CD_rules(v):
                w_fibword = fibword_from_index(w_index)
                i = words.index(w_fibword)
                value[i,j] += 1

        return value
