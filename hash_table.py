# Implementation of a hash table data structure
# By: Jacob Rockland

from doubly_linked_list import DoublyLinkedList

# hash table implementation using chaining to resolve collisions
class HashTableChaining(object):

    def __init__(self, size):
        self.size = size
        self.buckets = [None] * size

    def __repr__(self):
        pass # FIXME: Implement later

    def hash(self, key):
        return key % self.size

    def insert(self, item):
        bucket = self.buckets[self.hash(item.key)]
        if bucket is None:
            bucket = DoublyLinkedList()
        bucket.append(item)

    def remove(self, item):
        bucket = self.buckets[self.hash(item.key)]
        if bucket is None:
            bucket = DoublyLinkedList()
            return # item was not in hash table
        node = bucket.search(item)
        if node is not None:
            bucket.remove(node)

    def search(self, item):
        bucket = self.buckets[self.hash(item.key)]
        if bucket is None:
            return None # item was not in hash table
        else:
             return bucket.search(item)
