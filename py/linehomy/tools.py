class MyList(list):

    def __getitem__(self, key):

        # If len(self) == 1 then self[1] fails.
        while len(self) <= key:
            extras = self.next_items(key)
            self.extend(extras)

        return super().__getitem__(key)

    def next_items(self, key):

        return [self[-1] + self[-2]]
