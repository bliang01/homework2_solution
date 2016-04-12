import ctypes
import numpy
import os

from ctypes import (
    c_void_p,
    c_int,
    c_double,
)

# try to import the
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

    # produce pointers to underlying c arrays
    p_out = c_void_p(out.ctypes.data)
    p_x = c_void_p(x.ctypes.data)
    p_y = c_void_p(y.ctypes.data)
    int_N = c_int(N)

    # call
    try:
        homework2library.vec_add(p_out, p_x, p_y, int_N);
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

    # produce pointers to underlying c arrays
    p_out = c_void_p(out.ctypes.data)
    p_x = c_void_p(x.ctypes.data)
    p_y = c_void_p(y.ctypes.data)
    int_N = c_int(N)

    # call
    try:
        homework2library.vec_sub(p_out, p_x, p_y, int_N);
    except AttributeError:
        raise AttributeError("Something wrong happened when calling the C "
                             "library function.")
    return out


def vec_norm(x):
    # ensure data types of arrays are double and contiguize the result
    x = numpy.ascontiguousarray(x.astype(numpy.double))
    N = len(x)

    # produce pointers to underlying c arrays
    p_x = c_void_p(x.ctypes.data)
    int_N = c_int(N)

    # call
    try:
        # must explicitly set return type (since something is returned)
        homework2library.vec_norm.restype = c_double
        norm = homework2library.vec_norm(p_x, int_N);
    except AttributeError:
        raise AttributeError("Something wrong happened when calling the C "
                             "library function.")
    return norm

def mat_add(A, B):
    # ensure data types of arrays are double and contiguize the result
    A = numpy.ascontiguousarray(A.astype(numpy.double))
    B = numpy.ascontiguousarray(B.astype(numpy.double))
    out = numpy.empty_like(A)
    M_A,N_A = A.shape
    M_B,N_B = B.shape

    if (M_A != M_B) or (N_A != N_B):
        raise ValueError('Dimension mismatch.')

    # produce pointers to underlying c arrays
    p_out = c_void_p(out.ctypes.data)
    p_A = c_void_p(A.ctypes.data)
    p_B = c_void_p(B.ctypes.data)
    int_M = c_int(M_A)
    int_N = c_int(N_A)

    # call
    try:
        homework2library.mat_add(p_out, p_A, p_B, int_M, int_N);
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

    # produce pointers to underlying c arrays
    p_out = c_void_p(out.ctypes.data)
    p_A = c_void_p(A.ctypes.data)
    p_x = c_void_p(x.ctypes.data)
    int_M = c_int(M)
    int_N = c_int(N)

    # call
    try:
        homework2library.mat_vec(p_out, p_A, p_x, int_M, int_N);
    except AttributeError:
        raise AttributeError("Something wrong happened when calling the C "
                             "library function.")
    return out
