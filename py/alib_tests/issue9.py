from linhomy.cdrules import c_rule
from linhomy.cdrules import d_rule_2 as d_rule
from linhomy.cdrules import cd_trace_factory
from linhomy.cdrules import detect_collisions

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
