# Implementation of a doubly linked list data structure
# By: Jacob Rockland

# node class for doubly linked list
class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


# implementation of doubly linked list
class DoublyLinkedList(object):

    #initializes linked list
    def __init__(self, head = None, tail = None):
        self.head = head
        self.tail = tail

    # returns a string representation of linked list [data1, data2, ...]
    def __repr__(self):
        return repr(self.array())

    # returns an array representation of linked list
    def array(self):
        array = []
        curr = self.head
        while curr is not None:
            array.append(curr.data)
            curr = curr.next
        return array

    # returns an array representation of linked list in reverse
    def reverse_array(self):
        array = []
        curr = self.tail
        while curr is not None:
            array.append(curr.data)
            curr = curr.prev
        return array

    # adds node to end of list, O(1)
    def append(self, item):
        node = Node(item)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    # adds node to front of list, O(1)
    def prepend(self, item):
        node = Node(item)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node

    # inserts node into list after given position, O(1)
    def insert_after(self, curr, item):
        node = Node(item)
        if self.head is None:
            self.head = node
            self.tail = node
        elif curr is None:
            self.head.prev = node
            node.next = self.head
            self.head = node
        elif curr is self.tail:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        else:
            succ = curr.next
            node.next = succ
            node.prev = curr
            curr.next = node
            succ.prev = node

    # removes node from list after given position, O(1)
    def remove(self, curr):
        if self.head is None or curr is None:
            return
        else:
            succ = curr.next
            pred = curr.prev
            if succ is not None:
                succ.prev = pred
            if pred is not None:
                pred.next = succ
            if curr is self.head: # removed head
                self.head = succ
            if curr is self.tail: # removed tail
                self.tail = pred

    # searches for a given data value in list and returns first node if found, O(n)
    def search(self, key):
        curr = self.head
        while curr is not None:
            if curr.data == key:
                return curr
            curr = curr.next
        return None
