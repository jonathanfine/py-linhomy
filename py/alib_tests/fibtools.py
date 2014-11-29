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
