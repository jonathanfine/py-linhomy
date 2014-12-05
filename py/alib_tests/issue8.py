from linhomy.cdrules import Index
from linhomy.cdrules import c_rule


def do_index(s):

    i = Index(s)
    return [i.arg, i.mass, i.order]


do_index('') == ['', 0, 0]
do_index('00') == ['', 0, 0]
do_index('10') == ['10', 2, 0]
do_index('01') == ['01', 1, 0]
do_index(':') == [':', 3, 1]
do_index('00:00') == [':', 3, 1]
do_index('12:34') == ['12:34', 20, 1]


def do_c_rule(s):

    i = Index(s)
    value = c_rule(i)
    return [j.arg for j in value]

# Cones.
do_c_rule('') == ['01']
do_c_rule('01') == ['02']
do_c_rule('02') == ['03']

# Ds.
do_c_rule('10') == ['11', ':']
do_c_rule('20') == ['21', ':10', ':02']
do_c_rule('30') == ['31', ':20', ':12', ':04']

# As before, but order increased by one.
do_c_rule(':') == ['01:']
do_c_rule('01:') == ['02:']
do_c_rule('02:') == ['03:']

do_c_rule('10:') == ['11:', '::']
do_c_rule('20:') == ['21:', ':10:', ':02:']
do_c_rule('30:') == ['31:', ':20:', ':12:', ':04:']
