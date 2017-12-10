# coding: utf-8

from pyccelext.math.external_bsp import spl_compute_greville
from pyccelext.math.external_bsp import spl_eval_splines_ders


def test_greville():
    n_elements = 4
    p = 2
    n = p+n_elements

    m = n+p+1
    knots = zeros(m, double)
    for i in range(0, p+1):
        knots[i] = 0.0
    for i in range(p+1, n):
        knots[i] = (i-p) / n_elements
    for i in range(n, n+p+1):
        knots[i] = 1.0

    g = zeros(n, double)
    g = spl_compute_greville(n, p, knots)
    print(knots)
    print(g)

def test_eval_splines():
    n_elements = 4
    p = 2

    n = p+n_elements

    m = n+p+1
    knots = zeros(m, double)
    for i in range(0, p+1):
        knots[i] = 0.0
    for i in range(p+1, n):
        j = i-p
        knots[i] = j / n_elements
    for i in range(n, n+p+1):
        knots[i] = 1.0

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
    dN = spl_eval_splines_ders(p,m,d,r,knots,tau)

test_greville()
test_eval_splines()

print('> PASSED')
