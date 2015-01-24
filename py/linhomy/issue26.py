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
