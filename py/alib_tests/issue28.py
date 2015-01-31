from linhomy.issue28 import iter_deltas


def do_deltas(s):
    size_vec = list(map(int, s))
    return [
       ' '.join(
           ''.join(map(str, pair))
           for pair in item
        )
        for item in  iter_deltas(size_vec)
    ]


# Smoke tests.
do_deltas('') ** ValueError
do_deltas('0') == ['00']
do_deltas('1') == ['00']
do_deltas('2') == ['00']
