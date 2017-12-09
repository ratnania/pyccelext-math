# coding: utf-8

from pyccelext.math.quadratures import legendre

m = 3
x,w = legendre(m)
print(x)
print(w)
