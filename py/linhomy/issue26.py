def compose_3(n):
    '''Yield all non-negative solutions to i + j + k = n.

    Each solution is a composition of n into three parts.  The
    solutions are given in lexicographic order.  The number of
    solutions is (n + 2)(n + 1)/2, the binomial coefficient choose(n,
    n + 2).  Also the number of degree n monomials in three variables.

    '''
    m = n + 1
    for i in range(m):
        for j in range(m -i):
            yield i, j, n - i - j
