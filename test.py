# Testing of various searching and sorting algorithms and data structures
# By: Jacob Rockland

import unittest
import searching
import sorting

class TestSearchMethods(unittest.TestCase):
    def test_linear_search(self):
        list_even = [1, 2, 3, 4, 5, 6, 7, 8]
        list_odd = [1, 2, 3, 4, 5, 6, 7]
        list_one = [1]
        self.assertEqual(searching.linear_search(list_even, 2), 2)
        self.assertEqual(searching.linear_search(list_even, 5), 5)
        self.assertEqual(searching.linear_search(list_even, 4), 4)
        self.assertEqual(searching.linear_search(list_even, 7), 7)
        self.assertEqual(searching.linear_search(list_even, 9), None)
        self.assertEqual(searching.linear_search(list_odd, 2), 2)
        self.assertEqual(searching.linear_search(list_odd, 5), 5)
        self.assertEqual(searching.linear_search(list_odd, 7), 7)
        self.assertEqual(searching.linear_search(list_odd, 9), None)
        self.assertEqual(searching.linear_search(list_one, 1), 1)
        self.assertEqual(searching.linear_search(list_one, 2), None)

    def test_binary_search(self):
        list_even = [1, 2, 3, 4, 5, 6, 7, 8]
        list_odd = [1, 2, 3, 4, 5, 6, 7]
        list_one = [1]
        self.assertEqual(searching.binary_search(list_even, 2), 2)
        self.assertEqual(searching.binary_search(list_even, 5), 5)
        self.assertEqual(searching.binary_search(list_even, 4), 4)
        self.assertEqual(searching.binary_search(list_even, 7), 7)
        self.assertEqual(searching.binary_search(list_even, 9), None)
        self.assertEqual(searching.binary_search(list_odd, 2), 2)
        self.assertEqual(searching.binary_search(list_odd, 5), 5)
        self.assertEqual(searching.binary_search(list_odd, 7), 7)
        self.assertEqual(searching.binary_search(list_odd, 9), None)
        self.assertEqual(searching.binary_search(list_one, 1), 1)
        self.assertEqual(searching.binary_search(list_one, 2), None)

class TestSortMethods(unittest.TestCase):
    def test_selection_sort(self):
        list_a = [3, 1, 5, 4, 2, 0, -1]
        list_b = [5, 4, 3, 2, 1, 0, -1]
        list_c = [-1, 0, 1, 2, 3, 4, 5]
        list_d = [2, -1, 4, 1, 0, 5, 3]
        list_one = [1]
        list_sorted = [-1, 0, 1, 2, 3, 4, 5]
        sorting.selection_sort(list_a)
        sorting.selection_sort(list_b)
        sorting.selection_sort(list_c)
        sorting.selection_sort(list_d)
        sorting.selection_sort(list_one)
        self.assertEqual(list_a, list_sorted)
        self.assertEqual(list_b, list_sorted)
        self.assertEqual(list_c, list_sorted)
        self.assertEqual(list_d, list_sorted)
        self.assertEqual(list_one, list_one)

    def test_bubble_sort(self):
        list_a = [3, 1, 5, 4, 2, 0, -1]
        list_b = [5, 4, 3, 2, 1, 0, -1]
        list_c = [-1, 0, 1, 2, 3, 4, 5]
        list_d = [2, -1, 4, 1, 0, 5, 3]
        list_one = [1]
        list_sorted = [-1, 0, 1, 2, 3, 4, 5]
        sorting.bubble_sort(list_a)
        sorting.bubble_sort(list_b)
        sorting.bubble_sort(list_c)
        sorting.bubble_sort(list_d)
        sorting.bubble_sort(list_one)
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
        sorting.insertion_sort(list_a)
        sorting.insertion_sort(list_b)
        sorting.insertion_sort(list_c)
        sorting.insertion_sort(list_d)
        sorting.insertion_sort(list_one)
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
        sorting.quick_sort(list_a)
        sorting.quick_sort(list_b)
        sorting.quick_sort(list_c)
        sorting.quick_sort(list_d)
        sorting.quick_sort(list_one)
        self.assertEqual(list_a, list_sorted)
        self.assertEqual(list_b, list_sorted)
        self.assertEqual(list_c, list_sorted)
        self.assertEqual(list_d, list_sorted)
        self.assertEqual(list_one, list_one)

if __name__ == '__main__':
    unittest.main()
