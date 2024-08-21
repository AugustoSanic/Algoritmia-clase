"""
Unit testing for merge sort.
"""

import unittest
from mergesort import merge_sort


class TestMergeSort(unittest.TestCase):
    
    def test_empty_array(self):
        self.assertEqual(merge_sort([]), [])

    def test_single_element_array(self):
        self.assertEqual(merge_sort([7]), [7])

    def test_sorted_array(self):
        self.assertEqual(merge_sort([4, 7, 9]), [4, 7, 9])

    def test_unsorted_array(self):
        self.assertEqual(merge_sort([12, 7, 7, 20, 10, 10, 5]), [5, 7, 7, 10, 10, 12, 20])

    def test_array_with_duplicates(self):
        self.assertEqual(merge_sort([8, 8, 8, 3, 3, 3]), [3, 3, 3, 8, 8, 8])
    
    def test_array_with_negatives(self):
        self.assertEqual(merge_sort([12, -15, 12, -2, 3, 3]), [-15, -2, 3, 3, 12, 12])
    
    def test_array_with_floats(self):
        self.assertEqual(merge_sort([7.5, 2.0, -4.4]), [-4.4, 2.0, 7.5])


if __name__ == '__main__':
    unittest.main()
