import unittest
import numpy
from numpy import array
from numpy.linalg import norm

from homework2 import (
    vec_add,
)

class TestLinalg(unittest.TestCase):
    def test_vecadd(self):
        x = array([1,2,3])
        y = array([4,5,6])
        z = vec_add(x,y)
        self.assertAlmostEqual(norm(z - (x+y)), 0)


if __name__ == '__main__':
    unittest.main(verbosity=2) # run the above tests
