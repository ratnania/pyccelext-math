# coding: utf-8

#$ header make_knots(int, int)
def make_knots(n,p):
    n_elements = n-p
    m = n+p+1
    knots = zeros(m, double)
    for i in range(0, p+1):
        knots[i] = 0.0
    for i in range(p+1, n):
        j = i-p
        knots[i] = j / n_elements
    for i in range(n, n+p+1):
        knots[i] = 1.0
    return knots

#$ header make_greville(*double [:], int, int)
def make_greville(knots, n, p):
    greville = zeros(n, double)
    for i in range(0, n):
        s = 0.0
        for j in range(i+1, i+p+1):
            s = s + knots[j]
        greville[i] = s / p
    return greville
