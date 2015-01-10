from .issue4tools import fib_zeros_array

class Structure:

    def __init__(self, c_rules, d_rules):

        self.c_d_rules = [c_rules, d_rules]

        self._aaa = []


    def g_from_CD(self, n):

        cache = self._aaa

        m = len(cache)
        while len(cache) <= n:
            m = len(cache)
            value = fib_zeros_array(m, m)
            cache.append(value)

        return cache[n]


    # Based on cdrules g_from_CD.
    def _g_from_CD(self, word):

        ddt                     # Perhaps not yet finished.

        prev = [b'']

        for i in reversed(word):

            curr = []
            rules = self.c_d_rules[n]

            for item in prev:
                curr.extend(rules(item))

            prev = curr

        return prev
