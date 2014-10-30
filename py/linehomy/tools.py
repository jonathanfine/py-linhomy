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
