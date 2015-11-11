# Implementation of a stack ADT using a singly linked list
# By: Jacob Rockland

from singly_linked_list import SinglyLinkedList

# implementation of stack
class Stack(object):

    # initializes stack
    def __init__(self):
        self.__linked_list = SinglyLinkedList()
        self.length = 0

    # returns string representation of stack as "[item1, item2, ...]"
    def __repr__(self):
        return repr(self.__linked_list)

    # returns boolean value of whether or not stack is empty
    def is_empty(self):
        return True if self.length == 0 else False

    # returns length of stack
    def get_length(self):
        return self.length

    # pushes new item to top of stack
    def push(self, item):
        self.__linked_list.prepend(item)
        self.length += 1

    # returns item at top of stack and removes it
    def pop(self):
        item = self.__linked_list.head.data
        self.__linked_list.remove_after(None)
        self.length -= 1
        return item

    # returns item at the top of stack without removing
    def peek(self):
        return self.__linked_list.head.data
