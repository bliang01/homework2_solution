import unittest
import numpy
from numpy import array
from numpy.linalg import norm
from numpy.random import randn

from homework2 import (
    vec_add,
    vec_sub,
    vec_norm,
    mat_add,
    mat_vec,
)

class TestLinalg(unittest.TestCase):
    def test_vec_add(self):
        x = array([1,2,3])
        y = array([4,5,6])
        z = vec_add(x,y)
        error = norm(z - (x+y))
        self.assertAlmostEqual(error, 0)

    def test_vec_sub(self):
        x = array([1,2,3])
        y = array([4,5,6])
        z = vec_sub(x,y)
        error = norm(z - (x-y))
        self.assertAlmostEqual(error, 0)

    def test_vec_norm(self):
        x = array([1,2,3])
        n_actual = norm(x)
        n = vec_norm(x)
        self.assertAlmostEqual(n_actual, n)

    def test_mat_add(self):
        A = randn(5,5)
        B = randn(5,5)
        C = mat_add(A,B)
        error = norm(C - (A+B))
        self.assertAlmostEqual(error, 0)

    def test_mat_vec(self):
        A = randn(5,5)
        x = randn(5)
        y_actual = A.dot(x)
        y = mat_vec(A,x)
        error = norm(y - y_actual)
        self.assertAlmostEqual(error, 0)


if __name__ == '__main__':
    unittest.main(verbosity=2) # run the above tests
