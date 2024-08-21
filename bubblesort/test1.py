"""
Unit testing for bubble sort.
"""

import unittest
from bublesort import bubble_sort
from bubblesortoptimizada import bubble_sort_opt


class TestBubbleSort(unittest.TestCase):
    
    def test_base_empty_array(self):
        self.assertEqual(bubble_sort([]), [])

    def test_base_single_element_array(self):
        self.assertEqual(bubble_sort([5]), [5])

    def test_base_sorted_array(self):
        self.assertEqual(bubble_sort([3, 5, 8]), [3, 5, 8])

    def test_base_unsorted_array(self):
        self.assertEqual(bubble_sort([10, 5, 15, 2, 7, 20, 13]), [2, 5, 7, 10, 13, 15, 20])

    def test_base_array_with_duplicates(self):
        self.assertEqual(bubble_sort([10, 5, 15, 2, 5, 15, 20]), [2, 5, 5, 10, 15, 15, 20])
    
    def test_base_array_with_negatives(self):
        self.assertEqual(bubble_sort([10, 5, -15, -3, 7, 20, 13]), [-15, -3, 5, 7, 10, 13, 20])

    def test_opt_empty_array(self):
        self.assertEqual(bubble_sort_opt([]), [])

    def test_opt_single_element_array(self):
        self.assertEqual(bubble_sort_opt([5]), [5])

    def test_opt_sorted_array(self):
        self.assertEqual(bubble_sort_opt([3, 5, 8]), [3, 5, 8])

    def test_opt_unsorted_array(self):
        self.assertEqual(bubble_sort_opt([10, 5, 15, 2, 7, 20, 13]), [2, 5, 7, 10, 13, 15, 20])

    def test_opt_array_with_duplicates(self):
        self.assertEqual(bubble_sort_opt([10, 5, 15, 2, 5, 15, 20]), [2, 5, 5, 10, 15, 15, 20])
    
    def test_opt_array_with_negatives(self):
        self.assertEqual(bubble_sort_opt([10, 5, -15, -3, 7, 20, 13]), [-15, -3, 5, 7, 10, 13, 20])


if __name__ == '__main__':
    unittest.main()
