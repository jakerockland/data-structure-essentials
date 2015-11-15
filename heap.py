# Implementation of min and max heap data structures
# By: Jacob Rockland

# implementation of heap sort returning list in accending order, O(n*log(n))
def heap_sort_accending(items):
    heap = MinHeap(items)
    sorted = [heap.extract_min() for i in range(heap.size)]
    return sorted


# implementation of heap sort returning list in decending order, O(n*log(n))
def heap_sort_decending(items):
    heap = MaxHeap(items)
    sorted = [heap.extract_max() for i in range(heap.size)]
    return sorted


# implementation of min-heap
class MinHeap(object):

    # initialize heap
    def __init__(self, items = None):
        if items is None:
            self.heap_list = [None]
            self.size = 0
        else:
            self.build_heap(items)

    # returns string representation of heap
    def __repr__(self):
        temp = self.heap_list[1:]
        return repr(temp)

    # builds a heap from a given list of items, O(n)
    def build_heap(self, items):
        index = len(items) // 2
        self.size = len(items)
        self.heap_list = [None] + items[:]
        while index > 0:
            self.percolate_down(index)
            index -= 1

    # returns minimum item in heap, O(1)
    def get_min(self):
        if self.size > 0:
            return self.heap_list[1]
        else:
            return None

    # inserts a data item into the tree, O(log(n))
    def insert(self, data):
        self.heap_list.append(data)
        self.size += 1
        self.percolate_up(self.size)

    # percolates item in heap list upwards
    def percolate_up(self, index):
        # percolates upwards so long as current node is smaller than parent
        while index // 2 > 0:
            if self.heap_list[index] < self.heap_list[index // 2]:
                temp = self.heap_list[index // 2]
                self.heap_list[index // 2] = self.heap_list[index]
                self.heap_list[index] = temp
            index = index // 2

    # extract the minimum item in heap, O(log(n))
    def extract_min(self):
        if self.size > 0:
            min_val = self.heap_list[1]
            self.heap_list[1] = self.heap_list[self.size]
            self.size -= 1
            self.heap_list.pop()
            self.percolate_down(1)
            return min_val
        else:
            return None

    # percolates item in heap list downwards
    def percolate_down(self, index):
        # percolates downwards so long as current node is greater than child
        while index * 2 <= self.size:
            min = self.min_child(index)
            if self.heap_list[index] > self.heap_list[min]:
                temp = self.heap_list[index]
                self.heap_list[index] = self.heap_list[min]
                self.heap_list[min] = temp
            index = min

    # returns index of smallest child of subtree
    def min_child(self, index):
        if index * 2 + 1 > self.size:
            return index * 2
        elif self.heap_list[index * 2] < self.heap_list[index * 2 + 1]:
            return index * 2
        else:
            return index * 2 + 1


# implementation of max-heap
class MaxHeap(object):

    # initialize heap
    def __init__(self, items = None):
        if items is None:
            self.heap_list = [None]
            self.size = 0
        else:
            self.build_heap(items)

    # returns string representation of heap
    def __repr__(self):
        temp = self.heap_list[1:]
        return repr(temp)

    # builds a heap from a given list of items, O(n)
    def build_heap(self, items):
        index = len(items) // 2
        self.size = len(items)
        self.heap_list = [None] + items[:]
        while index > 0:
            self.percolate_down(index)
            index -= 1

    # returns maximum item in heap, O(1)
    def get_max(self):
        if self.size > 0:
            return self.heap_list[1]
        else:
            return None

    # inserts a data item into the tree, O(log(n))
    def insert(self, data):
        self.heap_list.append(data)
        self.size += 1
        self.percolate_up(self.size)

    # percolates item in heap list upwards
    def percolate_up(self, index):
        # percolates upwards so long as current node is greater than parent
        while index // 2 > 0:
            if self.heap_list[index] > self.heap_list[index // 2]:
                temp = self.heap_list[index // 2]
                self.heap_list[index // 2] = self.heap_list[index]
                self.heap_list[index] = temp
            index = index // 2

    # exctract the maximum item in heap, O(log(n))
    def extract_max(self):
        if self.size > 0:
            max_val = self.heap_list[1]
            self.heap_list[1] = self.heap_list[self.size]
            self.size -= 1
            self.heap_list.pop()
            self.percolate_down(1)
            return max_val
        else:
            return None

    # percolates item in heap list downwards
    def percolate_down(self, index):
        # percolates downwards so long as current node is smaller than child
        while index * 2 <= self.size:
            max = self.max_child(index)
            if self.heap_list[index] < self.heap_list[max]:
                temp = self.heap_list[index]
                self.heap_list[index] = self.heap_list[max]
                self.heap_list[max] = temp
            index = max

    # returns index of greatest child of subtree
    def max_child(self, index):
        if index * 2 + 1 > self.size:
            return index * 2
        elif self.heap_list[index * 2] > self.heap_list[index * 2 + 1]:
            return index * 2
        else:
            return index * 2 + 1
