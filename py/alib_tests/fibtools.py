from linhomy.fibtools import shift_1
from linhomy.fibtools import shift_1_pairs

from linhomy.fibtools import slide_1
from linhomy.fibtools import slide_1_pairs


def do_shift_1_pairs(length):

    return list(shift_1_pairs(length))


do_shift_1_pairs(2) == []
do_shift_1_pairs(4) == [(0, 0), (0, 2)]
do_shift_1_pairs(6) == [(0, 0), (0, 2), (0, 4), (2, 2), (2, 4)]
do_shift_1_pairs(8) == [
    (0, 0), (0, 2), (0, 4), (0, 6),
    (2, 2), (2, 4), (2, 6),
    (4, 4), (4, 6),
]


def do_shift_1(shape_str):

    shape_data = list(map(int, shape_str))

    return list(
        ''.join(str(i) for i in value)
        for value in shift_1(shape_data)
    )


do_shift_1('00') == []
do_shift_1('22') == []

do_shift_1('1000') == []
do_shift_1('1010') == ['0001']

do_shift_1('2000') == ['0100']
do_shift_1('2100') == ['0200']

do_shift_1('2010') == ['0110', '1001']
do_shift_1('2110') == ['0210', '1101']

do_shift_1('101010') == [
    '000110', '001001',
    '100001'
]

do_shift_1('202020') == [
    '012020', '101120', '102011',
    '200120', '201011',
]


from linhomy.fibtools import shift

def do_shift(shape_str):

    shape_data = list(map(int, shape_str))

    return list(
        ''.join(str(i) for i in value)
        for value in shift(shape_data)
    )


do_shift('23') == ['23']
do_shift('2100') == ['2100', '0200']
do_shift('4000') == ['4000', '2100', '0200']
do_shift('4010') == ['4010', '3001', '2110', '1101', '0210']
do_shift('4020') == ['4020', '3011', '2120', '2002', '1111', '0220', '0102']


def do_slide_1_pairs(length):

    return list(slide_1_pairs(length))

do_slide_1_pairs(2) == []
do_slide_1_pairs(4) == [(0, 2)]
do_slide_1_pairs(6) == [(0, 2), (0, 4), (2, 4)]
do_slide_1_pairs(8) == [
    (0, 2), (0, 4), (0, 6),
    (2, 4), (2, 6),
    (4, 6),
]


def do_slide_1(shape_str):

    shape_data = list(map(int, shape_str))

    return list(
        ''.join(str(i) for i in value)
        for value in slide_1(shape_data)
    )

do_slide_1('00') == []
do_slide_1('22') == []
do_slide_1('0022') == []
do_slide_1('0222') == []
do_slide_1('1000') == ['0010']

do_slide_1('100000') == ['001000', '000010']
do_slide_1('200000') == ['101000', '100010']

do_slide_1('001000') == ['000010']
do_slide_1('002000') == ['001010']


from linhomy.fibtools import slide

def do_slide(shape_str):

    shape_data = list(map(int, shape_str))

    return list(
        ''.join(str(i) for i in value)
        for value in slide(shape_data)
    )

do_slide('00') == ['00']
do_slide('1000') == ['1000', '0010']
do_slide('2000') == ['2000', '1010', '0020']
do_slide('3000') == ['3000', '2010', '1020', '0030']
do_slide('202000') == [
    '202000', '201010', '200020',
    '103000', '102010', '101020', '100030',
    '004000',
    '003010', '002020', '001030',
    '000040',
]


if 1:
    # TODO: Remove or refactor?
    # This explains the algorithm, produces binomial coefficients.
    from linhomy.fibtools import AAA
    aaa = AAA()
    aaa[0, 0] = 1
    aaa[3, 4] == 35
    # Produces binomial coefficients.
    list(aaa[i, 5-i] for i in range(0, 6)) == [1, 5, 10, 10, 5, 1]


from linhomy.fibtools import shuffle

def do_shuffle(i, j):

    return tuple(
        ''.join(str(i) for i in value)
        for value in shuffle(i, j)
    )


do_shuffle(0, 0) == ('',)

do_shuffle(0, 1) == ('2',)
do_shuffle(1, 0) == ('1',)

do_shuffle(0, 2) == ('22',)
do_shuffle(1, 1) == ('12', '21')
do_shuffle(2, 0) == ('11',)

do_shuffle(3, 4) == (
    # Prefix '1112'.
    '1112222',
    # Prefix '112'.
    '1121222', '1122122', '1122212', '1122221',
    # Prefix '121'.
    '1211222', '1212122', '1212212', '1212221',
    # Prefix '1221'.
    '1221122', '1221212', '1221221', '1222112', '1222121', '1222211',
    # Prefix '2112'.
    '2111222', '2112122', '2112212', '2112221',
    # Prefix '212'.
    '2121122', '2121212', '2121221', '2122112', '2122121', '2122211',
    # Prefix '221'.
    '2211122', '2211212', '2211221', '2212112', '2212121', '2212211',
    # Prefix '222'.
    '2221112', '2221121', '2221211',
    # Prefix '22221'.
    '2222111',
)

sorted(do_shuffle(3, 4)) == list(do_shuffle(3, 4))


from linhomy.fibtools import compute

# compute([2,2,3,1]) == None

def do_compute(shape_data):

    return list(
        ''.join(str(i) for i in value)
        for value in compute(shape_data)
    )

do_shift('2000') == ['2000', '0100']
do_slide('2000') == ['2000', '1010', '0020']
do_slide('0100') == ['0100']

do_compute([2, 0, 0, 0]) == ['221', '2111', '1211', '1121']



# TODO: Check these expected values.
do_compute([2, 2]) == [
    '2211', '2121', '2112',
    '1221', '1212', '1122'
]

do_compute([3, 0, 0, 0]) == [
    '2211', '2121', '21111',
    '1221', '12111', '11211', '11121'
]

do_compute([1, 0, 0, 1]) == ['2121', '2112', '1212']

do_compute([1, 0, 2, 0]) == ['2121', '2112', '21111', '12111']
