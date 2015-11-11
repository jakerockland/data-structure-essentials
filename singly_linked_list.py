# Implementation of a singly linked list data structure
# By: Jacob Rockland

# node class for linked list
class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None


# implementation of singly linked list
class SinglyLinkedList(object):

    # initializes linked list
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

    # adds node to end of list
    def append(self, item):
        node = Node(item)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    # adds node to front of list
    def prepend(self, item):
        node = Node(item)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node

    # inserts node into list after given position
    def insert_after(self, curr, item):
        node = Node(item)
        if self.head is None:
            self.head = node
            self.tail = node
        elif curr is None:
            node.next = self.head
            self.head = node
        elif curr is self.tail:
            self.tail.next = node
            self.tail = node
        else:
            node.next = curr.next
            curr.next = node

    # removes node from list after given position
    def remove_after(self, curr):
        if self.head is None:
            return
        elif curr is None:
            succ = self.head.next
            self.head = succ
            if succ is None: # checks if removed last item
                self.tail = None
        elif curr.next is not None:
            succ = curr.next.next
            curr.next = succ
            if succ is None: # checks if removed tail item
                self.tail = curr

    # searches for a given data value in list and returns first node if found
    def search(self, key):
        curr = self.head
        while curr is not None:
            if curr.data == key:
                return curr
            curr = curr.next
        return None
