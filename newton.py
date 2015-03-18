from numpy.polynomial.polynomial import polyval
from scipy.optimize import newton
from random import random

def poly(coeffs):
    def polyfunc(x):
        return polyval(x, coeffs)
    return polyfunc

def solve(coeffs, x0=0):
    return newton(poly(coeffs), x0)
