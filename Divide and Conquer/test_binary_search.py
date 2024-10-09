
'''
Pruebas unitarias para binarysearch.
'''

import unittest
from binary_search import binary_search

class PruebasBusquedaBinaria(unittest.TestCase):

    def setUp(self):
        self.test_arr = [3, 5, 9, 11, 13, 17, 19, 23, 27, 31, 35, 39, 42, 47]

    def test_elemento_presente(self):
        # Verifica que se encuentra un elemento presente en el arreglo
        self.assertEqual(binary_search(self.test_arr, 11), 3)
        self.assertEqual(binary_search(self.test_arr, 19), 6)
        self.assertEqual(binary_search(self.test_arr, 23), 7)
        self.assertEqual(binary_search(self.test_arr, 39), 11)

    def test_elemento_ausente(self):
        #  para un elemento que no está en el arreglo devolver-1
        self.assertEqual(binary_search(self.test_arr, 50), -1)
        self.assertEqual(binary_search(self.test_arr, 1), -1)

if __name__ == '__main__':
    unittest.main()

