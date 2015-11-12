# Testing of various searching and sorting algorithms and data structures
# By: Jacob Rockland

import unittest

import searching
import sorting

from singly_linked_list import SinglyLinkedList
from doubly_linked_list import DoublyLinkedList

from stack import Stack
from queue import Queue

from hash_table import HashTableChaining, HashTableLinearProbing

from binary_search_tree import BinarySearchTree

# test methods for BST implementation using linear probing
class TestBinarySearchTree(unittest.TestCase):

    def setUp(self):
        self.tree = BinarySearchTree()

    def test_basic_initialization_and_repr(self):
        self.assertEqual(repr(self.tree), '')

    def test_insert(self):
        self.tree.insert('C')
        self.assertEqual(repr(self.tree), 'C ')
        self.tree.insert('D')
        self.assertEqual(repr(self.tree), 'C D ')
        self.tree.insert('A')
        self.assertEqual(repr(self.tree), 'A C D ')
        self.tree.insert('B')
        self.assertEqual(repr(self.tree), 'A B C D ')
        self.tree.insert('F')
        self.assertEqual(repr(self.tree), 'A B C D F ')
        self.tree.insert('E')
        self.assertEqual(repr(self.tree), 'A B C D E F ')

    def test_search(self):
        self.tree.insert('C')
        self.tree.insert('D')
        self.tree.insert('A')
        self.tree.insert('B')
        self.tree.insert('F')
        self.tree.insert('E')
        self.assertEqual(self.tree.search('A').data, 'A')
        self.assertEqual(self.tree.search('B').data, 'B')
        self.assertEqual(self.tree.search('C').data, 'C')
        self.assertEqual(self.tree.search('D').data, 'D')
        self.assertEqual(self.tree.search('E').data, 'E')
        self.assertEqual(self.tree.search('F').data, 'F')
        self.assertEqual(self.tree.search('G'), None)

    def test_remove(self):
        self.tree.insert('C')
        self.tree.insert('D')
        self.tree.insert('A')
        self.tree.insert('B')
        self.tree.insert('F')
        self.tree.insert('E')
        self.assertEqual(repr(self.tree), 'A B C D E F ')
        self.tree.remove('E')
        self.assertEqual(repr(self.tree), 'A B C D F ')
        self.tree.remove('B')
        self.assertEqual(repr(self.tree), 'A C D F ')
        self.tree.remove('A')
        self.assertEqual(repr(self.tree), 'C D F ')
        self.tree.remove('C')
        self.assertEqual(repr(self.tree), 'D F ')
        self.tree.remove('D')
        self.assertEqual(repr(self.tree), 'F ')
        self.tree.remove('F')
        self.assertEqual(repr(self.tree), '')

    def test_in_order(self):
        self.tree.insert('F')
        self.tree.insert('G')
        self.tree.insert('B')
        self.tree.insert('A')
        self.tree.insert('D')
        self.tree.insert('I')
        self.tree.insert('H')
        self.tree.insert('E')
        self.tree.insert('C')
        self.assertEqual(self.tree.in_order(self.tree.root), 'A B C D E F G H I ')

    def test_pre_order(self):
        self.tree.insert('F')
        self.tree.insert('G')
        self.tree.insert('B')
        self.tree.insert('A')
        self.tree.insert('D')
        self.tree.insert('I')
        self.tree.insert('H')
        self.tree.insert('E')
        self.tree.insert('C')
        self.assertEqual(self.tree.pre_order(self.tree.root), 'F B A D C E G I H ')

    def test_post_order(self):
        self.tree.insert('F')
        self.tree.insert('G')
        self.tree.insert('B')
        self.tree.insert('A')
        self.tree.insert('D')
        self.tree.insert('I')
        self.tree.insert('H')
        self.tree.insert('E')
        self.tree.insert('C')
        self.assertEqual(self.tree.post_order(self.tree.root), 'A C E D B H I G F ')


# test methods for hash table implementation using linear probing
class TestHashTableLinearProbing(unittest.TestCase):

    class Item(object):

        def __init__(self, item):
            self.item = item
            self.key = item

        def __repr__(self):
            return repr(self.item)

        def __eq__(self, other):
            if isinstance(other, self.__class__):
                return self.item == other.item
            else:
                return False

    def setUp(self):
        self.hash_table = HashTableLinearProbing(5)

    def test_basic_initialization_and_repr(self):
        self.assertEqual(repr(self.hash_table), '[False, False, False, False, False]')

    def test_hash(self):
        self.assertEqual(self.hash_table.hash(17), 2)
        self.assertEqual(self.hash_table.hash(27), 2)
        self.assertEqual(self.hash_table.hash(12), 2)
        self.assertEqual(self.hash_table.hash(14), 4)
        self.assertEqual(self.hash_table.hash(1), 1)
        self.assertEqual(self.hash_table.hash(13), 3)
        self.assertEqual(self.hash_table.hash(20), 0)

    def test_insert(self):
        self.hash_table.insert(self.Item(3))
        self.assertEqual(repr(self.hash_table), '[False, False, False, 3, False]')
        self.hash_table.insert(self.Item(11))
        self.assertEqual(repr(self.hash_table), '[False, 11, False, 3, False]')
        self.hash_table.insert(self.Item(23))
        self.assertEqual(repr(self.hash_table), '[False, 11, False, 3, 23]')
        self.hash_table.insert(self.Item(33))
        self.assertEqual(repr(self.hash_table), '[33, 11, False, 3, 23]')
        self.hash_table.insert(self.Item(21))
        self.assertEqual(repr(self.hash_table), '[33, 11, 21, 3, 23]')

    def test_remove(self):
        self.hash_table.insert(self.Item(3))
        self.hash_table.insert(self.Item(11))
        self.hash_table.insert(self.Item(23))
        self.hash_table.insert(self.Item(33))
        self.assertEqual(repr(self.hash_table), '[33, 11, False, 3, 23]')
        self.hash_table.remove(33)
        self.assertEqual(repr(self.hash_table), '[True, 11, False, 3, 23]')
        self.hash_table.remove(21)
        self.assertEqual(repr(self.hash_table), '[True, 11, False, 3, 23]')
        self.hash_table.remove(21)
        self.assertEqual(repr(self.hash_table), '[True, 11, False, 3, 23]')
        self.hash_table.remove(11)
        self.assertEqual(repr(self.hash_table), '[True, True, False, 3, 23]')
        self.hash_table.remove(23)
        self.assertEqual(repr(self.hash_table), '[True, True, False, 3, True]')
        self.hash_table.remove(3)
        self.assertEqual(repr(self.hash_table), '[True, True, False, True, True]')

    def test_search(self):
        self.hash_table.insert(self.Item(3))
        self.hash_table.insert(self.Item(5))
        self.assertEqual(self.hash_table.search(4), None)
        self.assertEqual(self.hash_table.search(5), self.Item(5))


# test methods for hash table implementation using chaining
class TestHashTableChaining(unittest.TestCase):

    class Item(object):

        def __init__(self, item):
            self.item = item
            self.key = item

        def __repr__(self):
            return repr(self.item)

        def __eq__(self, other):
            if isinstance(other, self.__class__):
                return self.item == other.item
            else:
                return False

    def setUp(self):
        self.hash_table = HashTableChaining(5)

    def test_basic_initialization_and_repr(self):
        self.assertEqual(repr(self.hash_table), '[None, None, None, None, None]')

    def test_hash(self):
        self.assertEqual(self.hash_table.hash(17), 2)
        self.assertEqual(self.hash_table.hash(27), 2)
        self.assertEqual(self.hash_table.hash(12), 2)
        self.assertEqual(self.hash_table.hash(14), 4)
        self.assertEqual(self.hash_table.hash(1), 1)
        self.assertEqual(self.hash_table.hash(13), 3)
        self.assertEqual(self.hash_table.hash(20), 0)

    def test_insert(self):
        self.hash_table.insert(self.Item(3))
        self.assertEqual(repr(self.hash_table), '[None, None, None, [3], None]')
        self.hash_table.insert(self.Item(13))
        self.assertEqual(repr(self.hash_table), '[None, None, None, [3, 13], None]')
        self.hash_table.insert(self.Item(5))
        self.assertEqual(repr(self.hash_table), '[[5], None, None, [3, 13], None]')

    def test_remove(self):
        self.hash_table.insert(self.Item(3))
        self.hash_table.insert(self.Item(13))
        self.hash_table.insert(self.Item(5))
        self.assertEqual(repr(self.hash_table), '[[5], None, None, [3, 13], None]')
        self.hash_table.remove(self.Item(13))
        self.assertEqual(repr(self.hash_table), '[[5], None, None, [3], None]')
        self.hash_table.remove(self.Item(5))
        self.assertEqual(repr(self.hash_table), '[[], None, None, [3], None]')

    def test_search(self):
        self.hash_table.insert(self.Item(3))
        self.hash_table.insert(self.Item(5))
        self.assertEqual(self.hash_table.search(self.Item(4)), None)
        self.assertEqual(self.hash_table.search(self.Item(5)), self.Item(5))


# test methods for queue ADT
class TestQueue(unittest.TestCase):

    def setUp(self):
        self.queue = Queue()

    def test_basic_initialization_and_repr(self):
        self.assertEqual(repr(self.queue), '[]')

    def test_push(self):
        self.queue.push("!")
        self.assertEqual(repr(self.queue), "['!']")
        self.queue.push("world")
        self.assertEqual(repr(self.queue), "['!', 'world']")
        self.queue.push("Hello")
        self.assertEqual(repr(self.queue), "['!', 'world', 'Hello']")

    def test_pop(self):
        self.queue.push("!")
        self.queue.push("world")
        self.queue.push("Hello")
        self.assertEqual(repr(self.queue), "['!', 'world', 'Hello']")
        self.assertEqual(self.queue.pop(), '!')
        self.assertEqual(repr(self.queue), "['world', 'Hello']")
        self.assertEqual(self.queue.pop(), 'world')
        self.assertEqual(repr(self.queue), "['Hello']")

    def test_peek(self):
        self.queue.push("!")
        self.assertEqual(self.queue.peek(), '!')
        self.queue.push("world")
        self.assertEqual(self.queue.peek(), '!')

    def test_is_empty(self):
        self.assertTrue(self.queue.is_empty())
        self.queue.push("Hello world!")
        self.assertFalse(self.queue.is_empty())

    def test_get_length(self):
        self.assertEqual(self.queue.get_length(), 0)
        self.queue.push("Hello world!")
        self.assertEqual(self.queue.get_length(), 1)
        self.queue.push("Hello world!")
        self.assertEqual(self.queue.get_length(), 2)
        self.queue.pop()
        self.assertEqual(self.queue.get_length(), 1)
        self.queue.pop()
        self.assertEqual(self.queue.get_length(), 0)


# test methods for stack ADT
class TestStack(unittest.TestCase):

    def setUp(self):
        self.stack = Stack()

    def test_basic_initialization_and_repr(self):
        self.assertEqual(repr(self.stack), '[]')

    def test_push(self):
        self.stack.push("!")
        self.assertEqual(repr(self.stack), "['!']")
        self.stack.push("world")
        self.assertEqual(repr(self.stack), "['world', '!']")
        self.stack.push("Hello")
        self.assertEqual(repr(self.stack), "['Hello', 'world', '!']")

    def test_pop(self):
        self.stack.push("!")
        self.stack.push("world")
        self.stack.push("Hello")
        self.assertEqual(repr(self.stack), "['Hello', 'world', '!']")
        self.assertEqual(self.stack.pop(), 'Hello')
        self.assertEqual(repr(self.stack), "['world', '!']")
        self.assertEqual(self.stack.pop(), 'world')
        self.assertEqual(repr(self.stack), "['!']")

    def test_peek(self):
        self.stack.push('!')
        self.assertEqual(self.stack.peek(), '!')
        self.stack.push('world')
        self.assertEqual(self.stack.peek(), 'world')
        self.stack.push('Hello')
        self.assertEqual(self.stack.peek(), 'Hello')

    def test_is_empty(self):
        self.assertTrue(self.stack.is_empty())
        self.stack.push('Hello world!')
        self.assertFalse(self.stack.is_empty())

    def test_get_length(self):
        self.assertEqual(self.stack.get_length(), 0)
        self.stack.push('Hello world!')
        self.assertEqual(self.stack.get_length(), 1)
        self.stack.push('Hello world!')
        self.assertEqual(self.stack.get_length(), 2)
        self.stack.pop()
        self.assertEqual(self.stack.get_length(), 1)
        self.stack.pop()
        self.assertEqual(self.stack.get_length(), 0)


# test methods for doubly linked list
class TestDoublyLinkedList(unittest.TestCase):

    def setUp(self):
        self.my_list = DoublyLinkedList()

    def test_basic_initialization_and_repr(self):
        self.assertEqual(repr(self.my_list), '[]')

    def test_append(self):
        self.my_list.append(4)
        self.my_list.append(3)
        self.my_list.append(7)
        self.my_list.append(-17)
        self.assertEqual(repr(self.my_list), '[4, 3, 7, -17]')

    def test_prepend(self):
        self.my_list.prepend(4)
        self.my_list.prepend(3)
        self.my_list.prepend(7)
        self.my_list.prepend(-17)
        self.assertEqual(repr(self.my_list), '[-17, 7, 3, 4]')

    def test_insert_after(self):
        self.my_list.insert_after(None, 4)
        self.my_list.insert_after(None, 3)
        self.my_list.insert_after(self.my_list.tail, 7)
        self.my_list.insert_after(self.my_list.head, -17)
        self.assertEqual(repr(self.my_list), '[3, -17, 4, 7]')

    def test_remove(self):
        self.my_list.append(4)
        self.my_list.append(3)
        self.my_list.append(7)
        self.my_list.append(-17)
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
        self.my_list.append(4)
        self.my_list.append(3)
        self.my_list.append(7)
        self.my_list.append(-17)
        self.assertEqual(self.my_list.array(), [4, 3, 7, -17])

    def test_reverse_array(self):
        self.my_list.append(4)
        self.my_list.append(3)
        self.my_list.append(7)
        self.my_list.append(-17)
        self.assertEqual(self.my_list.reverse_array(), [-17, 7, 3, 4])

    def test_search(self):
        self.my_list.append(4)
        self.my_list.append(3)
        self.my_list.append(-17)
        self.my_list.append(7)
        self.assertEqual(self.my_list.search(4).data, 4)
        self.assertEqual(self.my_list.search(3).data, 3)
        self.assertEqual(self.my_list.search(-17).data, -17)
        self.assertEqual(self.my_list.search(17), None)


# test methods for singly linked list
class TestSinglyLinkedList(unittest.TestCase):

    def setUp(self):
        self.my_list = SinglyLinkedList()

    def test_basic_initialization_and_repr(self):
        self.assertEqual(repr(self.my_list), '[]')

    def test_append(self):
        self.my_list.append(4)
        self.my_list.append(3)
        self.my_list.append(7)
        self.my_list.append(-17)
        self.assertEqual(repr(self.my_list), '[4, 3, 7, -17]')

    def test_prepend(self):
        self.my_list.prepend(4)
        self.my_list.prepend(3)
        self.my_list.prepend(7)
        self.my_list.prepend(-17)
        self.assertEqual(repr(self.my_list), '[-17, 7, 3, 4]')

    def test_insert_after(self):
        self.my_list.insert_after(None, 4)
        self.my_list.insert_after(None, 3)
        self.my_list.insert_after(self.my_list.tail, 7)
        self.my_list.insert_after(self.my_list.head, -17)
        self.assertEqual(repr(self.my_list), '[3, -17, 4, 7]')

    def test_remove_after(self):
        self.my_list.append(4)
        self.my_list.append(3)
        self.my_list.append(7)
        self.my_list.append(-17)
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
        self.my_list.append(4)
        self.my_list.append(3)
        self.my_list.append(7)
        self.my_list.append(-17)
        self.assertEqual(self.my_list.array(), [4, 3, 7, -17])

    def test_search(self):
        self.my_list.append(4)
        self.my_list.append(3)
        self.my_list.append(-17)
        self.my_list.append(7)
        self.assertEqual(self.my_list.search(4).data, 4)
        self.assertEqual(self.my_list.search(3).data, 3)
        self.assertEqual(self.my_list.search(-17).data, -17)
        self.assertEqual(self.my_list.search(17), None)


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
