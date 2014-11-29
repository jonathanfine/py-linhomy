'''Tools for Fibonacci words and so on.

Contains
* tools for shapes

'''

def shift_1_pairs(length):
    for i in range(0, length - 2, 2):
        for j in range(i, length, 2):
            yield i, j


def shift_1(shape_data):

    length = len(shape_data)
    if length < 2 or length % 2:
        raise ValueError

    template = list(shape_data)
    value = template.copy()
    for i, j in shift_1_pairs(length):

        if i == j:
            if shape_data[i] >= 2:
                value[i] -= 2
                value[i+1] += 1
            else:
                continue
        else:
            if shape_data[i] >= 1 and shape_data[j] >= 1:
                value[i] -= 1
                value[j] -= 1
                value[j+1] += 1
            else:
                continue

        yield tuple(value)
        value = template.copy()


def slide_1_pairs(length):
    for i in range(0, length - 2, 2):
        for j in range(i + 2, length, 2):
            yield i, j


def slide_1(shape_data):

    # TODO: Uniform policy on checking argument.
    length = len(shape_data)
    template = list(shape_data)
    value = template.copy()
    for i, j in slide_1_pairs(length):

        if shape_data[i] >= 1:
            value[i] -= 1
            value[j] += 1
            yield tuple(value)
            value = template.copy()

if 1:
    # TODO: Remove or refactor?
    # This explains the algorithm, produces binomial coefficients.
    class AAA(dict):

        def __missing__(self, key):
            i, j = key
            if i == 0 or j == 0:
                return 1

            return sum(
                self[i - 1, k]
                for k in range(j + 1)
            )


class Shuffle(dict):

    def __init__(self, i_1, j_1):

        self.i_1 = i_1
        self.j_1 = j_1


    def __missing__(self, key):

        i, j = key
        i_1 = self.i_1
        j_1 = self.j_1
        if i == 0:
            return (j_1 * j,)

        if j == 0:
            return (i_1 * i,)


        value = []

        for k in range(j + 1):
            prefix = j_1 * k + i_1
            value.extend(
                prefix + suffix
                for suffix in self[i - 1, j - k]
            )

        return tuple(value)


_shuffle = Shuffle(b'\x01', b'\x02')

def shuffle(i, j):
    # TODO: Provide docstring.
    # TODO: Provide argument checks.
    return _shuffle[i, j]
