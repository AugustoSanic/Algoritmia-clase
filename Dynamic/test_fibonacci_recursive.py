'''
Pruebas unitarias para Fibonacci recursiva.
'''

import unittest
from fibonacci_recursive import fibonacci

class PruebasFibonacciRecursiva(unittest.TestCase):

    def test_numeros_pequenos(self):
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(10), 55)

    def test_numeros_medianos(self):
        self.assertEqual(fibonacci(15), 610)
        self.assertEqual(fibonacci(20), 6765)
    def test_numeros_grandes(self):
        self.assertEqual(fibonacci(20), 6765)
        self.assertEqual(fibonacci(30), 832040)
    def test10(self):
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)

if __name__ == '__main__':
    unittest.main()