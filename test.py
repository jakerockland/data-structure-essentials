# Testing of various searching and sorting algorithms and data structures
# By: Jacob Rockland

import unittest

from searching import linear_search, binary_search

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

if __name__ == '__main__':
    unittest.main()
