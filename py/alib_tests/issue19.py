from linhomy.issue19 import h_from_g_helper

def do_h_from_g(s):
    word = bytes(map(int, s))
    items = list(h_from_g_helper(word))
    return ' '.join(
        ''.join(map(str, w))
        for w in items
    )

do_h_from_g('') == ''
do_h_from_g('1') == '1'
do_h_from_g('2') == '2'

do_h_from_g('11') == '11 2'
do_h_from_g('12') == '12'
do_h_from_g('21') == '21'
do_h_from_g('22') == '22'

do_h_from_g('111') == '111 21'
do_h_from_g('211') == '211 22'

do_h_from_g('1112') == '1112 212'
do_h_from_g('2112') == '2112'

do_h_from_g('1111') == '1111 211 22'
do_h_from_g('211') == '211 22'
do_h_from_g('2112') == '2112'

do_h_from_g('11111') == '11111 2111 221'
do_h_from_g('2111') == '2111 221'
do_h_from_g('111112') == '111112 21112 2212'

do_h_from_g('112121') == '112121'
do_h_from_g('1112121') == '1112121 212121'
