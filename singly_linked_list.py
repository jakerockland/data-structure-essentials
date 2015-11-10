# Implementation of a singly linked list data structure
# By: Jacob Rockland

# node class for linked list
class Node(object):

    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next


def SinglyLinkedList(object):

    def __init__(self, head = None, tail = None):
        self.head = head
        self.tail = tail

    # adds node to end of list
    def append(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    # adds node to front of list
    def prepend(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = head
            self.head = node

    # inserts node into last after given position
    def insert_after(self, curr, node):
        if self.head is None:
            self.head = node
            self.tail = node
        elif curr is self.tail:
            self.tail.next = node
            self.tail = node
        else:
            node.next = curr.next
            curr.next = node
