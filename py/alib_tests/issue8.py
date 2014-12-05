from linhomy.cdrules import Index
from linhomy.cdrules import c_rule
from linhomy.cdrules import d_rule
from linhomy.cdrules import trace


def do_index(s):

    i = Index(s)
    return [i.arg, i.mass, i.order]


do_index('') == ['', 0, 0]
do_index('00') == ['', 0, 0]
do_index('10') == ['10', 2, 0]
do_index('01') == ['01', 1, 0]
do_index(':') == [':', 3, 1]
do_index('00:00') == [':', 3, 1]
do_index('12:34') == ['12:34', 17, 1]


def do_index_c_d(s):

    i = Index(s)
    c_i, d_i  = i.c, i.d
    if c_i.mass != i.mass + 1:
        raise ValueError
    if d_i.mass != i.mass + 2:
        raise ValueError

    return [c_i.arg, d_i.arg]


do_index_c_d('') == ['01', '10']
do_index_c_d('01') == ['02', '11']
do_index_c_d('10') == [':', '20']
do_index_c_d('11') == [':01', '21']

do_index_c_d(':') == ['01:', '10:']
do_index_c_d('01:') == ['02:', '11:']
do_index_c_d('10:') == ['::', '20:']
do_index_c_d('11:') == [':01:', '21:']


def do_c_rule(s):

    i = Index(s)
    value = c_rule(i)

    for j in value:
        if j.mass != i.mass + 1:
            # TODO: ValueError not right here.
            raise ValueError

    return [j.arg for j in value]

# The c_rule on cones.
do_c_rule('') == ['01']
do_c_rule('01') == ['02']
do_c_rule('02') == ['03']

# The d_rule on Ds.
do_c_rule('10') == ['11', ':']
do_c_rule('20') == ['21', ':10', ':02']
do_c_rule('30') == ['31', ':20', ':12', ':04']

do_c_rule('11') == ['12', ':01']


# As before, but order increased by one.
do_c_rule(':') == ['01:']
do_c_rule('01:') == ['02:']
do_c_rule('02:') == ['03:']

do_c_rule('10:') == ['11:', '::']
do_c_rule('20:') == ['21:', ':10:', ':02:']
do_c_rule('30:') == ['31:', ':20:', ':12:', ':04:']


def do_d_rule(s):

    i = Index(s)
    value = d_rule(i)

    for j in value:
        if j.mass != i.mass + 2:
            raise ValueError
        if j.order != i.order:
            raise ValueError

    return [j.arg for j in value]


# The d_rule on cones.
do_d_rule('') == ['10']
do_d_rule('01') == ['11']
do_d_rule('02') == ['12']

# The d_rule on Ds.
do_d_rule('10') == ['20']
do_d_rule('20') == ['30']
do_d_rule('30') == ['40']

# As before, but order increased by one.
do_d_rule(':') == ['10:', '01:01']

do_d_rule('01:') == ['11:', '02:01']
do_d_rule('02:') == ['12:', '03:01']


# The d_rule on Ds.
do_d_rule('10:') == ['20:']
do_d_rule('20:') == ['30:']
do_d_rule('30:') == ['40:']

# The d_rule on Ds.
do_d_rule('10::') == ['20::']
do_d_rule('20::') == ['30::']
do_d_rule('30::') == ['40::']


def tmp(i):
    return [i-1, i + 1]

trace(tmp, [[4], [8]]) == [
    [4, 3],
    [4, 5],
    [8, 7],
    [8, 9],
]


from linhomy.cdrules import cd_trace

def do_cd_trace(n):

    data = cd_trace(n)
    line_count = 0
    pairs = set()
    for key, val in cd_trace(n).items():
        line_count += len(val)

        pairs.update((key, line[-1].arg) for line in val)

    return [line_count, len(pairs)]

# These all agree with issue6.py.
do_cd_trace(0) == [1, 1]
do_cd_trace(1) == [1, 1]
do_cd_trace(2) == [2, 2]
do_cd_trace(3) == [4, 4]
do_cd_trace(4) == [8, 8]
do_cd_trace(5) == [18, 18]
do_cd_trace(6) == [40, 40]
do_cd_trace(7) == [91, 91]
do_cd_trace(8) == [208, 208]

# TODO: Investigate.  Could be consistent with test/issue6.py.
do_cd_trace(9) == [477, 475]    # 2 more lines, same number of errors.



def show_cd_trace(n):

    data = sorted(
        (key.arg, val)
        for key, val
        in cd_trace(n).items()
    )

    return [
        [key, sorted(line[-1].arg for line in val)]
        for key, val in data
    ]


## To document variation between the two values.

from linhomy.issue6 import c_rule as c_rule_aaa
from linhomy.issue6 import d_rule as d_rule_aaa
from linhomy.issue4tools import g_from_cd_rules_factory
from linhomy.constants import FIBWORDS
from linhomy.constants import FIB
from linhomy.cdrules import index_from_fibword

g_from_cd = g_from_cd_rules_factory(c_rule_aaa, d_rule_aaa)


def show_cd_trace_var(n):
    matrix = g_from_cd(n)
    lines = sorted(
        [
            index_from_fibword(FIBWORDS[n][i]).arg,
            sorted(
                index_from_fibword(FIBWORDS[n][j]).arg
                for j in range(FIB[n+1])
                if matrix[j, i] == 1
            )
        ]
        for i in range(FIB[n+1])
    )
    return lines


show_cd_trace(1) == show_cd_trace_var(1)
show_cd_trace(2) == show_cd_trace_var(2)
show_cd_trace(3) == show_cd_trace_var(3)
show_cd_trace(4) == show_cd_trace_var(4)
show_cd_trace(5) == show_cd_trace_var(5)

show_cd_trace(6) == [
    ['01:02', ['01:02', '14', ':03']],
    ['01:10', ['01:02', '01:10', '22', ':03', ':11']],
    ['02:01', ['01:02', '02:01', '14', ':03']],
    ['03:', ['01:02', '02:01', '03:', '14', ':03']],
    ['06', ['06']],
    ['10:01', ['01:02', '10:01', '22']],
    ['11:', ['01:02', '02:01', '10:01', '11:', '22']],
#    ['11:', ['01:02', '10:01', '11:', '22']],
    #                 ^ missing '02:01'.
    ['14', ['14']],
    ['22', ['22']],
    ['30', ['30']],
    [':03', ['14', ':03']],
    [':11', ['22', ':03', ':11']],
    ['::', ['02:01', '11:', '22', ':03', ':11', '::']],
]

# Here's how the line in question is calculated.
cd_trace(6)[Index('11:')] == [
    #           apply D      apply C      apply C       apply D
    [Index(''), Index('10'), Index('11'), Index('12'), Index('22')],
    [Index(''), Index('10'), Index('11'), Index(':01'), Index('10:01')],
    [Index(''), Index('10'), Index('11'), Index(':01'), Index('01:02')],
    [Index(''), Index('10'), Index(':'), Index('01:'), Index('11:')],
    [Index(''), Index('10'), Index(':'), Index('01:'), Index('02:01')],
]

# Here's why something is missing.
d_rule(Index('01:')) == (Index('11:'), Index('02:01'))

show_cd_trace_var(6) == [
    ['01:02', ['01:02', '14', ':03']],
    ['01:10', ['01:02', '01:10', '22', ':03', ':11']],
    ['02:01', ['01:02', '02:01', '14', ':03']],
    ['03:', ['01:02', '02:01', '03:', '14', ':03']],
    ['06', ['06']],
    ['10:01', ['01:02', '10:01', '22']],
    ['11:', ['01:02', '02:01', '10:01', '11:', '22']],
    #                  ^^^^^
    ['14', ['14']],
    ['22', ['22']],
    ['30', ['30']],
    [':03', ['14', ':03']],
    [':11', ['22', ':03', ':11']],
    ['::', ['02:01', '11:', '22', ':03', ':11', '::']],
]
