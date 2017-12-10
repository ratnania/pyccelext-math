# coding: utf-8

from pyccelext.math.external_bsp import spl_compute_greville

x = 1

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

g = zeros(n, double)
g = spl_compute_greville(n, p, knots)
print(knots)
print(g)
