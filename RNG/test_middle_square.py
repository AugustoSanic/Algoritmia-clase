'''
Pruebas para el método Middle Square.
'''

import unittest
import numpy as np
from rng_comparison import middle_square

class PruebasMiddleSquare(unittest.TestCase):

    def test_forma_de_salida(self):
        n = 90000
        seed = 1234
        ms_numbers = middle_square(n, seed).reshape((300, 300))
        self.assertEqual(ms_numbers.shape, (300, 300))

    def test_repetibilidad(self):
        n = 90000
        seed = 1234
        ms_numbers1 = middle_square(n, seed)
        ms_numbers2 = middle_square(n, seed)
        np.testing.assert_array_equal(ms_numbers1, ms_numbers2)

    def test_no_ceros(self):
        n = 1000
        seed = 1234
        ms_numbers = middle_square(n, seed)
        self.assertTrue(np.all(ms_numbers != 0)) 

if __name__ == '__main__':
    unittest.main()