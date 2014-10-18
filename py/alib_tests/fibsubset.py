from linehomy.fibsubset import iter_123_from_12

def t_123_12(items):
    '''Return tuple(iter_123_from_12(iter(items))).
    '''
    return tuple(iter_123_from_12(iter(items)))

t_123_12([]) == ()
