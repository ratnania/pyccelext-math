# coding: utf-8

from pyccelext.math.bsplines import make_knots
from pyccelext.math.bsplines import make_greville


def test_1():
    n_elements = 4
    p = 2
    n = p+n_elements

#    knots = make_knots(n, p)
#    print(" knots    = ", knots)
#
#    greville = make_greville(knots, n, p)
#    print(" greville = ", greville)

print('> PASSED')
