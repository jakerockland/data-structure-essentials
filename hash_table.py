# Implementation of a hash table data structure
# By: Jacob Rockland

from doubly_linked_list import DoublyLinkedList

# hash table implementation using chaining to resolve collisions
class HashTableChaining(object):

    # initializes hash table of given size
    def __init__(self, size):
        self.buckets = [None] * size
        self.size = size

    # returns string representation of hash table
    def __repr__(self):
        return repr(self.buckets)

    # performs hashing algorithm
    def hash(self, key):
        return key % self.size

    # inserts item into hash table
    def insert(self, item):
        bucket = self.buckets[self.hash(item.key)]
        if bucket is None:
            bucket = self.buckets[self.hash(item.key)] = DoublyLinkedList()
        bucket.append(item)

    # removes item from hash table, given hash item
    def remove(self, item):
        bucket = self.buckets[self.hash(item.key)]
        if bucket is None:
            return # item was not in hash table
        node = bucket.search(item)
        if node is not None:
            bucket.remove(node)

    # searches hash table for item, given hash item
    def search(self, item):
        bucket = self.buckets[self.hash(item.key)]
        if bucket is None:
            return None # item was not in hash table
        return bucket.search(item).data


# hash table implementation using linear probing to resolve collisions
class HashTableLinearProbing(object):

    # initializes hash table of given size
    def __init__(self, size):
        # False signifies an empty-since-start bucket
        # True signifies an empty-after-removal bucket
        self.buckets = [False] * size
        self.size = size

    # returns string representation of hash table
    def __repr__(self):
        return repr(self.buckets)

    # performs hashing algorithm
    def hash(self, key):
        return key % self.size

    # inserts item into hash table
    def insert(self, item):
        bucket_num = self.hash(item.key)
        num_probed = 0
        while num_probed < self.size:
            if self.buckets[bucket_num] is False or self.buckets[bucket_num] is True:
                self.buckets[bucket_num] = item
                return True
            bucket_num = (bucket_num + 1) % self.size
            num_probed += 1
        return False

    # removes item from hash table, given item key
    def remove(self, key):
        bucket_num = self.hash(key)
        num_probed = 0
        while num_probed < self.size and self.buckets[bucket_num] is not False  :
            if self.buckets[bucket_num] is not True and key == self.buckets[bucket_num].key:
                self.buckets[bucket_num] = True
                return
            bucket_num = (bucket_num + 1) % self.size
            num_probed += 1

    # searches hash table for item, given item key
    def search(self, key):
        bucket_num = self.hash(key)
        num_probed = 0
        while num_probed < self.size and self.buckets[bucket_num] is not False  :
            if self.buckets[bucket_num] is not True and key == self.buckets[bucket_num].key:
                return self.buckets[bucket_num]
            bucket_num = (bucket_num + 1) % self.size
            num_probed += 1
