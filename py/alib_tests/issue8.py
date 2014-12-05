from linhomy.cdrules import Index


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
