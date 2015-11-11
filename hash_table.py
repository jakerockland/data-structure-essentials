# Implementation of a hash table data structure
# By: Jacob Rockland

from doubly_linked_list import DoublyLinkedList

# hash table implementation using chaining to resolve collisions
class HashTableChaining(object):

    def __init__(self, size):
        self.buckets = [None] * size
        self.size = size

    def __repr__(self):
        string = ""
        for bucket in self.buckets:
            string += repr(bucket) + ', '
        return "[%s]" % string[:-2]

    def hash(self, key):
        return key % self.size

    def insert(self, item):
        bucket = self.buckets[self.hash(item.key)]
        if bucket is None:
            bucket = self.buckets[self.hash(item.key)] = DoublyLinkedList()
        bucket.append(item)

    def remove(self, item):
        bucket = self.buckets[self.hash(item.key)]
        if bucket is None:
            return # item was not in hash table
        node = bucket.search(item)
        if node is not None:
            bucket.remove(node)

    def search(self, item):
        bucket = self.buckets[self.hash(item.key)]
        if bucket is None:
            return None # item was not in hash table
        return bucket.search(item).data


# hash table implementation using linear probing to resolve collisions
class HashTableLinearProbing(object):

    def __init__(self, size):
        # False signifies an empty-since-start bucket
        # True signifies an empty-after-removal bucket
        self.buckets = [False] * size
        self.size = size

    def __repr__(self):
        pass # FIXME: Implement later

    def hash(self, key):
        return key % self.size

    def insert(self, item):
        pass # FIXME: Implement later

    def remove(self, item):
        pass # FIXME: Implement later

    def search(self, item):
        pass # FIXME: Implement later
