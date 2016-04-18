import unittest
import numpy
from numpy import array
from numpy.linalg import norm
from numpy.random import randn
from scipy.linalg import solve_triangular as scipy_solve_triangular
from scipy.linalg import solve as scipy_solve

from homework2 import (
    vec_add,
    vec_sub,
    vec_norm,
    mat_add,
    mat_vec,
    solve_lower_triangular,
    solve_upper_triangular,
    jacobi,
    gauss_seidel,
)

def random_lower_triangular(n):
    L = randn(n,n)
    for i in range(n):
        for j in range(n):
            if i < j:
                L[i,j] = 0
    return L

def random_upper_triangular(n):
    U = randn(n,n)
    for i in range(n):
        for j in range(n):
            if i > j:
                U[i,j] = 0
    return U

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

class TestSolver(unittest.TestCase):
    def test_solve_lower_trangular(self):
        # create a random lower triangular matrix
        L = random_lower_triangular(5)
        b = randn(5)
        y_actual = scipy_solve_triangular(L,b,lower=True)
        y = solve_lower_triangular(L,b)
        error = norm(y - y_actual)
        self.assertAlmostEqual(error, 0)

    def test_solve_upper_trangular(self):
        # create a random upper triangular matrix
        U = random_upper_triangular(5)
        b = randn(5)
        y_actual = scipy_solve_triangular(U,b)
        y = solve_upper_triangular(U,b)
        error = norm(y - y_actual)
        self.assertAlmostEqual(error, 0)

    def test_jacobi(self):
        # create random sdd matrix
        A = randn(5,5) + numpy.diag(5*numpy.ones(5))
        b = randn(5)
        y_actual = scipy_solve(A,b)
        y,_ = jacobi(A,b)
        error = norm(y - y_actual)
        self.assertLess(error, 1e-4)

    def test_gauss_seidel(self):
        # create random sdd matrix
        A = randn(5,5) + numpy.diag(5*numpy.ones(5))
        b = randn(5)
        y_actual = scipy_solve(A,b)
        y,_ = gauss_seidel(A,b)
        error = norm(y - y_actual)
        self.assertLess(error, 1e-4)

    def test_convergence_rate(self):
        # tests to see if the student's Gauss-seidel function has the correct
        # related convergence rate to the Jacobi method. in other words, Jacobi
        # should converge faster
        n = 10
        A = randn(n,n) + numpy.diag(n*numpy.ones(n))
        b = randn(n)
        _,iter_jacobi = jacobi(A,b,epsilon=1e-12)
        _,iter_gs = gauss_seidel(A,b,epsilon=1e-12)

        print 'iter_jacobi:', iter_jacobi
        print 'iter_gs:', iter_gs
        self.assertLess(iter_gs, iter_jacobi)


def time_lower_triangular(n, number=3):
    # returns the time to perform a random nxn lower triangular solve
    from timeit import timeit

    s = '''
from numpy.random import randn
from homework2 import solve_lower_triangular
from test_homework2 import random_lower_triangular
N = %d
L = random_lower_triangular(N)
b = randn(N)
'''%(n)
    total_time = timeit('solve_lower_triangular(L,b)', setup=s, number=number)
    avg_time = total_time / number
    return avg_time

def time_upper_triangular(n, number=3):
    # returns the time to perform a random nxn upper triangular solve
    from timeit import timeit

    s = '''
from numpy.random import randn
from homework2 import solve_upper_triangular
from test_homework2 import random_upper_triangular
N = %d
L = random_upper_triangular(N)
b = randn(N)
'''%(n)
    total_time = timeit('solve_upper_triangular(L,b)', setup=s, number=number)
    avg_time = total_time / number
    return avg_time

def time_jacobi(n, number=1):
    # returns the average time to perform a random nxn lower triangular solve
    from timeit import timeit

    s = '''
from numpy import diag, ones
from numpy.random import randn
from homework2 import jacobi
N = %d
A = randn(N,N) + diag(N*ones(N))
b = randn(N)
'''%(n)
    total_time = timeit('jacobi(A,b)', setup=s, number=number)
    avg_time = total_time / number
    return avg_time

def time_gauss_seidel(n, number=1):
    # returns the average time to perform a random nxn lower triangular solve
    from timeit import timeit

    s = '''
from numpy import diag, ones
from numpy.random import randn
from homework2 import gauss_seidel
N = %d
A = randn(N,N) + diag(N*ones(N))
b = randn(N)
'''%(n)
    total_time = timeit('gauss_seidel(A,b)', setup=s, number=number)
    avg_time = total_time / number
    return avg_time


if __name__ == '__main__':
    #n = 2**13
    n = 2**10
    t = time_jacobi(n)
    print 'jacobi(%d): %f'%(n, t)

    t = time_gauss_seidel(n)
    print 'gauss_seidel(%d): %f'%(n, t)

    print '\n===== Running Tests ====='
    unittest.main(verbosity=2)
