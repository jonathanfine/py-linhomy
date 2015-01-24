import itertools

def compose_3(n):
    '''Yield all non-negative solutions to i + j + k = n.

    Each solution is a composition of n into three parts.  The
    solutions are given in lexicographic order.  The number of
    solutions is (n + 2)(n + 1)/2, the binomial coefficient choose(n,
    n + 2).  Also number of degree n monomials in three variables.
    '''

    m = n + 1
    for i in range(m):
        for j in range(m -i):
            yield i, j, n - i - j


def simple_remove(pairs, index, n):
    '''At index remove n, replace by spaces in same pair.

    Do nothing if n == 0, even if index is out of bounds.
    '''

    # Part of semantics - not here as an optimisation.
    if n:
        pairs[index][0] -= n        # Remove.
        pairs[index][1] += 2 * n    # Add all space here.


def slide_remove(pairs, index, n):
    '''At index remove n, replace by spaces in same and next pair.

    Do nothing if n == 0, even if index is out of bounds.
    '''

    # Part of semantics - not here as an optimisation.
    if n:
        pairs[index][0] -= n        # Remove.
        pairs[index][1] += n        # Add half space here.
        pairs[index + 1][1] += n    # And other half at next.


def make_removal_argv(available):
    '''Return argv for use with itertools.product.

    This is a helper function.
    '''

    # Deal with special case: zero or one pairs.
    if len(available) < 2:
        # Will result in only trivial removal (leave the same).
        return [(0, 0)] * len(available)

    # First and last pairs are treated differently.
    first, body, last = available[0], available[1:-1], available[-1]

    argv = []                   # Accumulator.

    # On first pair, only slide_remove allowed.
    argv.append(tuple(
        (0, i) for i in range(first + 1)
    ))

    # On body, both slide_remove and simple_remove allowed.
    for size in body:
        argv.append(tuple(
            (i, j)
            for i, j, k in compose_3(size)
        ))

    # On last pair, only simple remove allowed.
    argv.append(tuple(
        (i, 0) for i in range(last + 1)
    ))

    return argv
