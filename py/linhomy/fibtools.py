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
    for i,j in shift_1_pairs(length):

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
