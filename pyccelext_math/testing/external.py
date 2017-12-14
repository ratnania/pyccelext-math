# coding: utf-8

# todo: improve these tests using arrays/lists

from pyccelext.math.external.bsp import spl_compute_greville
from pyccelext.math.external.bsp import spl_eval_splines_ders

from pyccelext.math.external.blas import saxpy
from pyccelext.math.external.blas import daxpy

def test_blas_saxpy():
    n = 5
    sa = 1.0

    incx = 1
    sx = zeros(n, float)

    incy = 1
    sy = zeros(n, float)

    sx[0] = 1.0
    sx[1] = 3.0
    sx[3] = 5.0

    sy[0] = 2.0
    sy[1] = 4.0
    sy[3] = 6.0

    saxpy(n, sa, sx, incx, sy, incy)

def test_blas_daxpy():
    n = 5
    sa = 1.0

    incx = 1
    sx = zeros(n, double)

    incy = 1
    sy = zeros(n, double)

    sx[0] = 1.0
    sx[1] = 3.0
    sx[3] = 5.0

    sy[0] = 2.0
    sy[1] = 4.0
    sy[3] = 6.0

    daxpy(n, sa, sx, incx, sy, incy)

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

test_blas_saxpy()
test_blas_daxpy()

test_greville()
test_eval_splines()

print('> PASSED')
