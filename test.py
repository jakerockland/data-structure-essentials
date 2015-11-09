# Testing of various searching and sorting algorithms and data structures
# By: Jacob Rockland

import unittest

from searching import linear_search, binary_search
from sorting import selection_sort, insertion_sort, quick_sort

class TestSearchMethods(unittest.TestCase):
    def test_linear_search(self):
        list_even = [1, 2, 3, 4, 5, 6, 7, 8]
        list_odd = [1, 2, 3, 4, 5, 6, 7]
        list_one = [1]
        self.assertEqual(linear_search(list_even, 2), 2)
        self.assertEqual(linear_search(list_even, 5), 5)
        self.assertEqual(linear_search(list_even, 4), 4)
        self.assertEqual(linear_search(list_even, 7), 7)
        self.assertEqual(linear_search(list_even, 9), None)
        self.assertEqual(linear_search(list_odd, 2), 2)
        self.assertEqual(linear_search(list_odd, 5), 5)
        self.assertEqual(linear_search(list_odd, 7), 7)
        self.assertEqual(linear_search(list_odd, 9), None)
        self.assertEqual(linear_search(list_one, 1), 1)
        self.assertEqual(linear_search(list_one, 2), None)

    def test_binary_search(self):
        list_even = [1, 2, 3, 4, 5, 6, 7, 8]
        list_odd = [1, 2, 3, 4, 5, 6, 7]
        list_one = [1]
        self.assertEqual(binary_search(list_even, 2), 2)
        self.assertEqual(binary_search(list_even, 5), 5)
        self.assertEqual(binary_search(list_even, 4), 4)
        self.assertEqual(binary_search(list_even, 7), 7)
        self.assertEqual(binary_search(list_even, 9), None)
        self.assertEqual(binary_search(list_odd, 2), 2)
        self.assertEqual(binary_search(list_odd, 5), 5)
        self.assertEqual(binary_search(list_odd, 7), 7)
        self.assertEqual(binary_search(list_odd, 9), None)
        self.assertEqual(binary_search(list_one, 1), 1)
        self.assertEqual(binary_search(list_one, 2), None)

class TestSortMethods(unittest.TestCase):
    def test_selection_sort(self):
        list_a = [3, 1, 5, 4, 2, 0, -1]
        list_b = [5, 4, 3, 2, 1, 0, -1]
        list_c = [-1, 0, 1, 2, 3, 4, 5]
        list_d = [2, -1, 4, 1, 0, 5, 3]
        list_one = [1]
        list_sorted = [-1, 0, 1, 2, 3, 4, 5]
        selection_sort(list_a)
        selection_sort(list_b)
        selection_sort(list_c)
        selection_sort(list_d)
        selection_sort(list_one)
        self.assertEqual(list_a, list_sorted)
        self.assertEqual(list_b, list_sorted)
        self.assertEqual(list_c, list_sorted)
        self.assertEqual(list_d, list_sorted)
        self.assertEqual(list_one, list_one)

    def test_insertion_sort(self):
        list_a = [3, 1, 5, 4, 2, 0, -1]
        list_b = [5, 4, 3, 2, 1, 0, -1]
        list_c = [-1, 0, 1, 2, 3, 4, 5]
        list_d = [2, -1, 4, 1, 0, 5, 3]
        list_one = [1]
        list_sorted = [-1, 0, 1, 2, 3, 4, 5]
        insertion_sort(list_a)
        insertion_sort(list_b)
        insertion_sort(list_c)
        insertion_sort(list_d)
        insertion_sort(list_one)
        self.assertEqual(list_a, list_sorted)
        self.assertEqual(list_b, list_sorted)
        self.assertEqual(list_c, list_sorted)
        self.assertEqual(list_d, list_sorted)
        self.assertEqual(list_one, list_one)

    def test_quick_sort(self):
        list_a = [3, 1, 5, 4, 2, 0, -1]
        list_b = [5, 4, 3, 2, 1, 0, -1]
        list_c = [-1, 0, 1, 2, 3, 4, 5]
        list_d = [2, -1, 4, 1, 0, 5, 3]
        list_one = [1]
        list_sorted = [-1, 0, 1, 2, 3, 4, 5]
        quick_sort(list_a)
        quick_sort(list_b)
        quick_sort(list_c)
        quick_sort(list_d)
        quick_sort(list_one)
        self.assertEqual(list_a, list_sorted)
        self.assertEqual(list_b, list_sorted)
        self.assertEqual(list_c, list_sorted)
        self.assertEqual(list_d, list_sorted)
        self.assertEqual(list_one, list_one)

if __name__ == '__main__':
    unittest.main()
