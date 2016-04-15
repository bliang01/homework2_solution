import ctypes
import numpy
import os

from ctypes import (
    c_void_p,
    c_int,
    c_double,
)

# try to import the library
try:
    path_to_library = os.path.join('lib','homework2.so')
    homework2library = ctypes.cdll.LoadLibrary(path_to_library)
except OSError:
    raise OSError("You need to compile your homework library using 'make'.")


def vec_add(x, y):
    # ensure data types of arrays are double and contiguize the result
    x = numpy.ascontiguousarray(x.astype(numpy.double))
    y = numpy.ascontiguousarray(y.astype(numpy.double))
    out = numpy.empty_like(x)
    N = len(x)

    # set function types and call on data
    try:
        homework2library.vec_add.restype = c_void_p
        homework2library.vec_add.argtypes = [c_void_p, c_void_p, c_void_p, c_int]
        homework2library.vec_add(out.ctypes.data, x.ctypes.data, y.ctypes.data, N);
    except AttributeError:
        raise AttributeError("Something wrong happened when calling the C "
                             "library function.")
    return out

def vec_sub(x, y):
    # ensure data types of arrays are double and contiguize the result
    x = numpy.ascontiguousarray(x.astype(numpy.double))
    y = numpy.ascontiguousarray(y.astype(numpy.double))
    out = numpy.empty_like(x)
    N = len(x)

    # set function types and call on data
    try:
        homework2library.vec_sub.restype = c_void_p
        homework2library.vec_sub.argtypes = [c_void_p, c_void_p, c_void_p, c_int]
        homework2library.vec_sub(
            out.ctypes.data, x.ctypes.data, y.ctypes.data, N);
    except AttributeError:
        raise AttributeError("Something wrong happened when calling the C "
                             "library function.")
    return out


def vec_norm(x):
    # ensure data types of arrays are double and contiguize the result
    x = numpy.ascontiguousarray(x.astype(numpy.double))
    N = len(x)

    # set function types and call on data
    try:
        homework2library.vec_norm.restype = c_double
        homework2library.vec_norm.argtypes = [c_void_p, c_int]
        norm = homework2library.vec_norm(x.ctypes.data, N);
    except AttributeError:
        raise AttributeError("Something wrong happened when calling the C "
                             "library function.")
    return norm

def mat_add(A, B):
    # ensure data types of arrays are double and contiguize the result
    A = numpy.ascontiguousarray(A.astype(numpy.double))
    B = numpy.ascontiguousarray(B.astype(numpy.double))
    out = numpy.empty_like(A)
    M_A, N_A = A.shape
    M_B, N_B = B.shape

    if (M_A != M_B) or (N_A != N_B):
        raise ValueError('Dimension mismatch.')

    # set function types and call on data
    try:
        homework2library.mat_add.restype = c_void_p
        homework2library.mat_add.argtypes = [
            c_void_p, c_void_p, c_void_p, c_int, c_int]
        homework2library.mat_add(
            out.ctypes.data, A.ctypes.data, B.ctypes.data, M_A, N_A);
    except AttributeError:
        raise AttributeError("Something wrong happened when calling the C "
                             "library function.")
    return out


def mat_vec(A, x):
    # ensure data types of arrays are double and contiguize the result
    A = numpy.ascontiguousarray(A.astype(numpy.double))
    x = numpy.ascontiguousarray(x.astype(numpy.double))
    out = numpy.empty_like(x)
    M,N = A.shape

    if (N != len(x)):
        raise ValueError('Dimension mismatch.')

    # set function types and call on data
    try:
        homework2library.mat_vec.restype = c_void_p
        homework2library.mat_vec.argtypes = [
            c_void_p, c_void_p, c_void_p, c_int, c_int]
        homework2library.mat_vec(
            out.ctypes.data, A.ctypes.data, x.ctypes.data, M, N)
    except AttributeError:
        raise AttributeError("Something wrong happened when calling the C "
                             "library function.")
    return out

def solve_lower_triangular(L, b):
    # ensure that the data types of arrays are double and contiuguize the result
    L = numpy.ascontiguousarray(L.astype(numpy.double))
    b = numpy.ascontiguousarray(b.astype(numpy.double))
    out = numpy.empty_like(b)
    M,N = L.shape

    if (M != N):
        raise ValueError('Matrix L must be square.')
    if (N != len(b)):
        raise ValueError('Dimension mismatch')

    # set function types and call on data
    try:
        homework2library.solve_lower_triangular.restype = c_void_p
        homework2library.solve_lower_triangular.argtypes = [
            c_void_p, c_void_p, c_void_p, c_int]
        homework2library.solve_lower_triangular(
            out.ctypes.data, L.ctypes.data, b.ctypes.data, N)
    except AttributeError:
        raise AttributeError("Something wrong happened when calling the C "
                             "library function.")
    return out

def solve_upper_triangular(U, b):
    # ensure that the data types of arrays are double and contiuguize the result
    U = numpy.ascontiguousarray(U.astype(numpy.double))
    b = numpy.ascontiguousarray(b.astype(numpy.double))
    out = numpy.empty_like(b)
    M,N = U.shape

    if (M != N):
        raise ValueError('Matrix U must be square.')
    if (N != len(b)):
        raise ValueError('Dimension mismatch')

    # set function types and call on data
    try:
        homework2library.solve_upper_triangular.restype = c_void_p
        homework2library.solve_upper_triangular.argtypes = [
            c_void_p, c_void_p, c_void_p, c_int]
        homework2library.solve_upper_triangular(
            out.ctypes.data, U.ctypes.data, b.ctypes.data, N)
    except AttributeError:
        raise AttributeError("Something wrong happened when calling the C "
                             "library function.")
    return out
