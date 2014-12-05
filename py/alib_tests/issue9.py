from linhomy.cdrules import c_rule
from linhomy.cdrules import d_rule_2 as d_rule
from linhomy.cdrules import cd_trace_factory
from linhomy.cdrules import detect_collisions
from linhomy.cdrules import args_from_collisions
from linhomy.cdrules import Index

cd_trace = cd_trace_factory(c_rule, d_rule)

def doit(n):

    trace = cd_trace(n)
    return detect_collisions(trace)


doit(4) == {}
doit(5) == {}
doit(6) == {}
doit(7) == {}
doit(8) == {}
len(doit(9)) == 1
len(doit(10)) == 8
len(doit(11)) == 43


cd_trace(5) == {
    Index('10:'): [
        [Index(''), Index('10'), Index('11'), Index('21')],
        [Index(''), Index('10'), Index(':'), Index('10:')],
        [Index(''), Index('10'), Index(':'), Index('01:01')]
    ],
    Index('13'): [
        [Index(''), Index('01'), Index('02'), Index('03'), Index('13')]
    ],
    Index(':02'): [
        [Index(''), Index('01'), Index('02'), Index('12'), Index('13')],
        [Index(''), Index('01'), Index('02'), Index('12'), Index(':02')]
    ],
    Index('02:'): [
        [Index(''), Index('10'), Index('11'), Index('12'), Index('13')],
        [Index(''), Index('10'), Index('11'), Index('12'), Index(':02')],
        [Index(''), Index('10'), Index('11'), Index(':01'), Index('01:01')],
        [Index(''), Index('10'), Index(':'), Index('01:'), Index('02:')]
    ],
    Index('01:01'): [
        [Index(''), Index('01'), Index('11'), Index('12'), Index('13')],
        [Index(''), Index('01'), Index('11'), Index('12'), Index(':02')],
        [Index(''), Index('01'), Index('11'), Index(':01'), Index('01:01')]
    ],
    Index('21'): [
        [Index(''), Index('01'), Index('11'), Index('21')]
    ],
    Index(':10'): [
        [Index(''), Index('10'), Index('20'), Index('21')],
        [Index(''), Index('10'), Index('20'), Index(':10')],
        [Index(''), Index('10'), Index('20'), Index(':02')]
    ],
    Index('05'): [
        [Index(''), Index('01'), Index('02'), Index('03'), Index('04'), Index('05')]
    ]
}



def show_collisions(n):
    trace = cd_trace(n)
    collisions = detect_collisions(trace)
    return sorted(map(list, args_from_collisions(collisions).items()))


show_collisions(9) == [
    [
        (':11:', ':02:01'),
        [
            #     D     C     C       D        D         C
            ['', '10', '11', ':01', '10:01', '20:01', ':02:01'],
            ['', '10', ':', '01:', '02:01', '12:01', ':02:01']
        ]
    ]
]
