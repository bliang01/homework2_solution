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
