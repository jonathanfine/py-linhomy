if 1:
    # TODO: Remove this code?  It's not being used.
    ## 1. Use of Self-extending list
    from linhomy.tools import self_extending_list

    # This is a copy of code in linhomy/constants.py.
    @self_extending_list([0, 1])
    def FIB(self, key):
        '''The Fibonacci numbers 0, 1, 1, 2, 3, 5, 13, ...

        F(n) = F(n-1) + F(n-2) with F(0) = 1 and F(1) = 1.
        https://oeis.org/A000045
        '''
        return [self[-1] + self[-2]]

    FIB[0] == 0
    FIB[1] == 1
    FIB[2] == 1
    FIB[3] == 2
    FIB[10] == 55


    ## 2. Internal properties
    from linhomy.tools import SelfExtendingList
    type(FIB) == SelfExtendingList
    type(FIB + [1, 2, 3]) == list

    # TODO: Support slice access.
    list(range(7)[0:6:2]) == [0, 2, 4]
    FIB[0:6:2] ** TypeError

    # TODO: Prevent mutation.
    import operator
    operator.setitem([0, 1, 2], 1, 2) == None
    operator.setitem((0, 1, 2), 1, 2) ** TypeError
    operator.setitem(FIB, 1, 2) == None # Should be TypeError
    # Tests for del FIB[n].
    # Tests for slice assignment and deletion.
    # TODO: User MappingProxyType?  New in Python 3.3.
    # TODO: truncation, to reclaim memory.
    # TODO: Provide a reset property.


##

# TODO: I'm not using this - discard?
if 1:
    from linhomy.tools import missingdict

    @missingdict
    def missdict(self, key):

        value = key ** 2
        self[key] = value           # Needed to store value.
        return value

    list(missdict.items()) == []
    missdict[2] == 4
    list(missdict.items()) == [(2, 4)]
    missdict[3:6] ** TypeError      # "unhashable type: 'slice'"


##
from linhomy.tools import cache_function

@cache_function
def do_fib(cache, i):
    '''Return i-th Fibonacci number.'''

    if i >= 2:
        return cache[i-1] + cache[i-2]
    else:
        cache[0] = 0
        cache[1] = 1
        return cache[i]

# Note: do_fib called only when there is a cache miss.

do_fib.__name__ == 'do_fib'
do_fib.__doc__ == '''Return i-th Fibonacci number.'''

len(do_fib._cache) == 0

if 0:
    # TODO: Move these to alib.test.
    do_fib._cache == []         # TODO: Gives later value of _cache.
    2 in do_fib._cache          # TODO: Fails, with strange message.

do_fib(5) == 5
do_fib(6) == 8
len(do_fib._cache) == 7
