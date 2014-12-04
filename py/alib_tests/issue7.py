from linhomy.issue6 import d_rule_2 # TODO: Ugly names here.
from linhomy.fibsubset import Word
from linhomy.fibsubset import Shape


# TODO: Log and remove this gotcha.
Shape(b'\x02\01').arg == ';21'
Word(b'\x02\x01').worm.shape.arg == '00;00'


def do_d_rule_2(s):

    s = Shape(s)
    v =  b'' + s.word
    value = d_rule_2(v)
    return [Word(w).worm.shape.arg for w in value]

do_d_rule_2(';00') == []

do_d_rule_2('00;00') == ['10;10']

do_d_rule_2('10;00') == ['20;10']
do_d_rule_2('00;10') == ['10;20']

do_d_rule_2('20;00') == ['30;10']
do_d_rule_2('10;10') == ['20;20']
do_d_rule_2('00;20') == ['10;30']

do_d_rule_2('00;01') == []
do_d_rule_2('01;00') == ['11;10']

do_d_rule_2('30;00') == ['40;10']
do_d_rule_2('20;10') == ['30;20']
do_d_rule_2('10;20') == ['20;30']
do_d_rule_2('00;30') == ['10;40']

do_d_rule_2('10;01') == []
do_d_rule_2('00;11') == []
do_d_rule_2('11;00') == ['21;10']
do_d_rule_2('01;10') == ['11;20']


# TODO: This test should fail.
do_d_rule_2('00,00;00') == ['10,00;10', '10;10'] # Should fail.

# TODO: This test should pass.
do_d_rule_2('00,00;00') == ['10,00;10', '00,10;10'] # Should pass.
