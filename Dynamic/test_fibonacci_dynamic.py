

import unittest
from fibonacci_dynamic import fibonacci

class PruebasFibonacci(unittest.TestCase):

    def test_numeros_pequenos(self):
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(10), 55)

    def test_numeros_grandes(self):
        self.assertEqual(fibonacci(25), 75025)
        self.assertEqual(fibonacci(30), 832040)
    def test10(self):
        self.assertEqual(0, 0)  
        self.assertEqual(fibonacci(1), 1)
if __name__ == '__main__':
    unittest.main()