# Testing of various searching and sorting algorithms and data structures
# By: Jacob Rockland

import unittest
import searching
import sorting
from singly_linked_list import SinglyLinkedList, Node as SingleNode
from doubly_linked_list import DoublyLinkedList, Node as DoubleNode

# test methods for doubly linked list
class TestDoublyLinkedList(unittest.TestCase):

    def setUp(self):
        self.my_list = DoublyLinkedList()

    def test_basic_initialization_and_repr(self):
        self.assertEqual(repr(self.my_list), '[]')

    def test_append(self):
        self.my_list.append(DoubleNode(4))
        self.my_list.append(DoubleNode(3))
        self.my_list.append(DoubleNode(7))
        self.my_list.append(DoubleNode(-17))
        self.assertEqual(repr(self.my_list), '[4, 3, 7, -17]')

    def test_prepend(self):
        self.my_list.prepend(DoubleNode(4))
        self.my_list.prepend(DoubleNode(3))
        self.my_list.prepend(DoubleNode(7))
        self.my_list.prepend(DoubleNode(-17))
        self.assertEqual(repr(self.my_list), '[-17, 7, 3, 4]')

    def test_insert_after(self):
        self.my_list.insert_after(None, DoubleNode(4))
        self.my_list.insert_after(None, DoubleNode(3))
        self.my_list.insert_after(self.my_list.tail, DoubleNode(7))
        self.my_list.insert_after(self.my_list.head, DoubleNode(-17))
        self.assertEqual(repr(self.my_list), '[3, -17, 4, 7]')

    def test_remove(self):
        self.my_list.append(DoubleNode(4))
        self.my_list.append(DoubleNode(3))
        self.my_list.append(DoubleNode(7))
        self.my_list.append(DoubleNode(-17))
        self.assertEqual(repr(self.my_list), '[4, 3, 7, -17]')
        self.my_list.remove(self.my_list.head)
        self.assertEqual(repr(self.my_list), '[3, 7, -17]')
        self.my_list.remove(self.my_list.head.next)
        self.assertEqual(repr(self.my_list), '[3, -17]')
        self.my_list.remove(self.my_list.tail)
        self.assertEqual(repr(self.my_list), '[3]')
        self.my_list.remove(self.my_list.head)
        self.my_list.remove(self.my_list.head)
        self.assertEqual(repr(self.my_list), '[]')

    def test_array(self):
        self.my_list.append(DoubleNode(4))
        self.my_list.append(DoubleNode(3))
        self.my_list.append(DoubleNode(7))
        self.my_list.append(DoubleNode(-17))
        self.assertEqual(self.my_list.array(), [4, 3, 7, -17])

    def test_reverse_array(self):
        self.my_list.append(DoubleNode(4))
        self.my_list.append(DoubleNode(3))
        self.my_list.append(DoubleNode(7))
        self.my_list.append(DoubleNode(-17))
        self.assertEqual(self.my_list.reverse_array(), [-17, 7, 3, 4])


# test methods for singly linked list
class TestSinglyLinkedList(unittest.TestCase):

    def setUp(self):
        self.my_list = SinglyLinkedList()

    def test_basic_initialization_and_repr(self):
        self.assertEqual(repr(self.my_list), '[]')

    def test_append(self):
        self.my_list.append(SingleNode(4))
        self.my_list.append(SingleNode(3))
        self.my_list.append(SingleNode(7))
        self.my_list.append(SingleNode(-17))
        self.assertEqual(repr(self.my_list), '[4, 3, 7, -17]')

    def test_prepend(self):
        self.my_list.prepend(SingleNode(4))
        self.my_list.prepend(SingleNode(3))
        self.my_list.prepend(SingleNode(7))
        self.my_list.prepend(SingleNode(-17))
        self.assertEqual(repr(self.my_list), '[-17, 7, 3, 4]')

    def test_insert_after(self):
        self.my_list.insert_after(None, SingleNode(4))
        self.my_list.insert_after(None, SingleNode(3))
        self.my_list.insert_after(self.my_list.tail, SingleNode(7))
        self.my_list.insert_after(self.my_list.head, SingleNode(-17))
        self.assertEqual(repr(self.my_list), '[3, -17, 4, 7]')

    def test_remove_after(self):
        self.my_list.append(SingleNode(4))
        self.my_list.append(SingleNode(3))
        self.my_list.append(SingleNode(7))
        self.my_list.append(SingleNode(-17))
        self.assertEqual(repr(self.my_list), '[4, 3, 7, -17]')
        self.my_list.remove_after(None)
        self.assertEqual(repr(self.my_list), '[3, 7, -17]')
        self.my_list.remove_after(self.my_list.head)
        self.assertEqual(repr(self.my_list), '[3, -17]')
        self.my_list.remove_after(self.my_list.tail)
        self.assertEqual(repr(self.my_list), '[3, -17]')
        self.my_list.remove_after(None)
        self.my_list.remove_after(None)
        self.my_list.remove_after(None)
        self.assertEqual(repr(self.my_list), '[]')

    def test_array(self):
        self.my_list.append(SingleNode(4))
        self.my_list.append(SingleNode(3))
        self.my_list.append(SingleNode(7))
        self.my_list.append(SingleNode(-17))
        self.assertEqual(self.my_list.array(), [4, 3, 7, -17])


# test methods from sorting module
class TestSortMethods(unittest.TestCase):

    def setUp(self):
        self.list_a = [30, 13, 57, 42, 21, 0, -11]
        self.list_b = [57, 42, 30, 21, 13, 0, -11]
        self.list_c = [-11, 0, 13, 21, 30, 42, 57]
        self.list_d = [21, -11, 42, 13, 0, 57, 30]
        self.list_one = [1]
        self.list_two = [-5, -10]
        self.list_sorted = [-11, 0, 13, 21, 30, 42, 57]

    def test_selection_sort(self):
        sorting.selection_sort(self.list_a)
        sorting.selection_sort(self.list_b)
        sorting.selection_sort(self.list_c)
        sorting.selection_sort(self.list_d)
        sorting.selection_sort(self.list_one)
        sorting.selection_sort(self.list_two)
        self.assertEqual(self.list_a, self.list_sorted)
        self.assertEqual(self.list_b, self.list_sorted)
        self.assertEqual(self.list_c, self.list_sorted)
        self.assertEqual(self.list_d, self.list_sorted)
        self.assertEqual(self.list_one, [1])
        self.assertEqual(self.list_two, [-10, -5])

    def test_bubble_sort(self):
        sorting.bubble_sort(self.list_a)
        sorting.bubble_sort(self.list_b)
        sorting.bubble_sort(self.list_c)
        sorting.bubble_sort(self.list_d)
        sorting.bubble_sort(self.list_one)
        sorting.bubble_sort(self.list_two)
        self.assertEqual(self.list_a, self.list_sorted)
        self.assertEqual(self.list_b, self.list_sorted)
        self.assertEqual(self.list_c, self.list_sorted)
        self.assertEqual(self.list_d, self.list_sorted)
        self.assertEqual(self.list_one, [1])
        self.assertEqual(self.list_two, [-10, -5])

    def test_insertion_sort(self):
        sorting.insertion_sort(self.list_a)
        sorting.insertion_sort(self.list_b)
        sorting.insertion_sort(self.list_c)
        sorting.insertion_sort(self.list_d)
        sorting.insertion_sort(self.list_one)
        sorting.insertion_sort(self.list_two)
        self.assertEqual(self.list_a, self.list_sorted)
        self.assertEqual(self.list_b, self.list_sorted)
        self.assertEqual(self.list_c, self.list_sorted)
        self.assertEqual(self.list_d, self.list_sorted)
        self.assertEqual(self.list_one, [1])
        self.assertEqual(self.list_two, [-10, -5])

    def test_quick_sort(self):
        sorting.quick_sort(self.list_a)
        sorting.quick_sort(self.list_b)
        sorting.quick_sort(self.list_c)
        sorting.quick_sort(self.list_d)
        sorting.quick_sort(self.list_one)
        sorting.quick_sort(self.list_two)
        self.assertEqual(self.list_a, self.list_sorted)
        self.assertEqual(self.list_b, self.list_sorted)
        self.assertEqual(self.list_c, self.list_sorted)
        self.assertEqual(self.list_d, self.list_sorted)
        self.assertEqual(self.list_one, [1])
        self.assertEqual(self.list_two, [-10, -5])

    def test_merge_sort(self):
        sorting.merge_sort(self.list_a)
        sorting.merge_sort(self.list_b)
        sorting.merge_sort(self.list_c)
        sorting.merge_sort(self.list_d)
        sorting.merge_sort(self.list_one)
        sorting.merge_sort(self.list_two)
        self.assertEqual(self.list_a, self.list_sorted)
        self.assertEqual(self.list_b, self.list_sorted)
        self.assertEqual(self.list_c, self.list_sorted)
        self.assertEqual(self.list_d, self.list_sorted)
        self.assertEqual(self.list_one, [1])
        self.assertEqual(self.list_two, [-10, -5])

    def test_heap_sort(self):
        sorting.heap_sort(self.list_a)
        sorting.heap_sort(self.list_b)
        sorting.heap_sort(self.list_c)
        sorting.heap_sort(self.list_d)
        sorting.heap_sort(self.list_one)
        sorting.heap_sort(self.list_two)
        self.assertEqual(self.list_a, self.list_sorted)
        self.assertEqual(self.list_b, self.list_sorted)
        self.assertEqual(self.list_c, self.list_sorted)
        self.assertEqual(self.list_d, self.list_sorted)
        self.assertEqual(self.list_one, [1])
        self.assertEqual(self.list_two, [-10, -5])


# test methods from searching module
class TestSearchMethods(unittest.TestCase):

    def setUp(self):
        self.list_even = [1, 2, 3, 4, 5, 6, 7, 8]
        self.list_odd = [1, 2, 3, 4, 5, 6, 7]
        self.list_one = [1]

    def test_linear_search(self):
        self.assertEqual(searching.linear_search(self.list_even, 2), 2)
        self.assertEqual(searching.linear_search(self.list_even, 5), 5)
        self.assertEqual(searching.linear_search(self.list_even, 4), 4)
        self.assertEqual(searching.linear_search(self.list_even, 7), 7)
        self.assertEqual(searching.linear_search(self.list_even, 9), None)
        self.assertEqual(searching.linear_search(self.list_odd, 2), 2)
        self.assertEqual(searching.linear_search(self.list_odd, 5), 5)
        self.assertEqual(searching.linear_search(self.list_odd, 7), 7)
        self.assertEqual(searching.linear_search(self.list_odd, 9), None)
        self.assertEqual(searching.linear_search(self.list_one, 1), 1)
        self.assertEqual(searching.linear_search(self.list_one, 2), None)

    def test_binary_search(self):
        self.assertEqual(searching.binary_search(self.list_even, 2), 2)
        self.assertEqual(searching.binary_search(self.list_even, 5), 5)
        self.assertEqual(searching.binary_search(self.list_even, 4), 4)
        self.assertEqual(searching.binary_search(self.list_even, 7), 7)
        self.assertEqual(searching.binary_search(self.list_even, 9), None)
        self.assertEqual(searching.binary_search(self.list_odd, 2), 2)
        self.assertEqual(searching.binary_search(self.list_odd, 5), 5)
        self.assertEqual(searching.binary_search(self.list_odd, 7), 7)
        self.assertEqual(searching.binary_search(self.list_odd, 9), None)
        self.assertEqual(searching.binary_search(self.list_one, 1), 1)
        self.assertEqual(searching.binary_search(self.list_one, 2), None)


if __name__ == '__main__':
    unittest.main()
