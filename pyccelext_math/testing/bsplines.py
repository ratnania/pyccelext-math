# coding: utf-8

from pyccelext.math.bsplines import make_knots
from pyccelext.math.bsplines import make_greville

from pyccelext.math.external.bsp import spl_eval_splines_ders
from pyccelext.math.external.bsp import spl_compute_spans

def test_1():
    n_elements = 4
    p = 2
    n = p+n_elements

    knots = make_knots(n, p)
    print(" knots    = ", knots)

    greville = make_greville(knots, n, p)
    print(" greville = ", greville)

    spans = zeros(n_elements, int)
    basis_elements = zeros(n, int)

    # ... subroutine call
    [spans, basis_elements] = spl_compute_spans(p, n, knots)
    print(" spans = ", spans)
    print(" basis_elements = ", basis_elements)


def test_2():
    n_elements = 4
    p = 2
    n = p+n_elements

    knots = make_knots(n, p)
    print(" knots    = ", knots)

    d = 2
    r = 3
    r1 = r + 1
    p1 = p + 1
    d1 = d + 1

    tau = zeros(r1, double)
    tau[0] = 0.1
    tau[1] = 0.3
    tau[2] = 0.7
    tau[3] = 0.8

    dN = zeros((p1,d1,r1), double)
    dN = spl_eval_splines_ders(p,n,d,r,knots,tau)

    print(" dN = ", dN)

test_1()
test_2()

print('> PASSED')
