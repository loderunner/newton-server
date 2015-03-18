# newton-server: Simple Flask app server to solve polynomial equations using Newton's method
# Copyright (c) 2015 Charles Francoise
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from numpy.polynomial.polynomial import polyval
from scipy.optimize import newton
from random import random

def poly(coeffs):
    def polyfunc(x):
        return polyval(x, coeffs)
    return polyfunc

def solve(coeffs, x0=0):
    return newton(poly(coeffs), x0)
