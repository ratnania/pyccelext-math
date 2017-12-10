# coding: utf-8

from pyccelext.math.quadratures import legendre

def test_legendre():
    m = 3
    x,w = legendre(m)
    print(x)
    print(w)

#test_legendre()

print('> PASSED')

