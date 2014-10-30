from functools import partial

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
