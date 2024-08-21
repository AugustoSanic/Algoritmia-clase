"""
Unit testing for counting sort.
"""

import unittest
from countingsort import counting_sort


class TestCountingSort(unittest.TestCase):
    
    def test_empty_array(self):
        self.assertEqual(counting_sort([]), [])

    def test_single_element_array(self):
        self.assertEqual(counting_sort([7]), [7])

    def test_sorted_array(self):
        self.assertEqual(counting_sort([2, 4, 6]), [2, 4, 6])

    def test_unsorted_array(self):
        self.assertEqual(counting_sort([7, 3, 3, 10, 4, 4, 2]), [2, 3, 3, 4, 4, 7, 10])

    def test_array_with_duplicates(self):
        self.assertEqual(counting_sort([8, 8, 8, 2, 2, 2]), [2, 2, 2, 8, 8, 8])


if __name__ == '__main__':
    unittest.main()
