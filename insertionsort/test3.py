"""
Unit testing for insertion sort.
"""

import unittest
from insertionsort import insertion_sort


class TestInsertionSort(unittest.TestCase):
    
    def test_base_empty_array(self):
        self.assertEqual(insertion_sort([]), [])

    def test_base_single_element_array(self):
        self.assertEqual(insertion_sort([8]), [8])

    def test_base_sorted_array(self):
        self.assertEqual(insertion_sort([2, 4, 6]), [2, 4, 6])

    def test_base_unsorted_array(self):
        self.assertEqual(insertion_sort([10, 5, 14, 2, 7, 12, 8]), [2, 5, 7, 8, 10, 12, 14])

    def test_base_array_with_duplicates(self):
        self.assertEqual(insertion_sort([8, 4, 10, 2, 4, 10, 14]), [2, 4, 4, 8, 10, 10, 14])
    
    def test_base_array_with_negatives(self):
        self.assertEqual(insertion_sort([8, 4, -10, -3, 5, 12, 7]), [-10, -3, 4, 5, 7, 8, 12])


if __name__ == '__main__':
    unittest.main()
