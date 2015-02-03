from linhomy.issue30 import multiplicity_from_delta

def do_multiplicity(delta_s):

    delta = tuple(
        tuple(map(int, pair))
        for pair in delta_s.split(' ')
        )

    return multiplicity_from_delta(delta)


do_multiplicity('00') == 1
do_multiplicity('00 00') == 1
