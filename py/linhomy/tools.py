from functools import partial
import itertools
import operator

class SelfExtendingList(list):
    # TODO: Docstring.

    __slots__ = ['__doc__', 'next_items']

    def __getitem__(self, key):

        # If len(self) == 1 then self[1] fails.
        while len(self) <= key:
            extras = self.next_items(key)
            self.extend(extras)

        return super().__getitem__(key)


def self_extending_list(seed):
    # TODO: Docstring.

    def make_self_extending_list(fn):

        self = SelfExtendingList(seed)
        self.next_items = partial(fn, self)
        self.__doc__ = fn.__doc__

        return self

    return make_self_extending_list


# TODO: Do we keep this attempt to generalise cd_g_ones.
if 0:

    def iter_subset(fn, axes):
        '''Iterate over all points in subset defined by fn.

        Each axis is an iterable of (index, value) pairs.  Each yield
        provides a tuple of indices.
        '''

        get_index = operator.itemgetter(0)
        get_value = operator.itemgetter(1)

        for point in itertools.product(*axes):

            value = fn(*map(get_value, point))
            if value:
                yield tuple(map(get_index, point))

# TODO: I'm not using this - discard?
if 1:
    def missingdict(fn):

        class Nameless(dict):

            __missing__ = fn

        Nameless.__name__ = fn.__name__
        value = Nameless()
        return value


def cache_function(value_from_key):

    class cls(dict):

        def __missing__(self, key):

            value = value_from_key(self, key)
            self[key] = value
            return value

    cache = cls()

    def fn(*argv):

        # Adapt between function call and dictionary conventions.
        if len(argv) == 1:
            key = argv[0]
        else:
            key = arg

        return cache[key]

    # TODO: Add wrapped function? Consistent with functools?
    fn.__doc__ = value_from_key.__doc__
    fn.__name__ = value_from_key.__name__
    fn._cache = cache

    return fn
