# Implementation of a trie tree data structure
# By: Jacob Rockland

# node class for trie tree
class Node(object):

    # initializes node
    def __init__(self, value = None):
        self.value = value
        self.children = set()

    # returns True if node is a leaf (has no children), False otherwise
    def is_leaf(self):
        return len(self.children) == 0


# implementation of trie tree
class TrieTree(object):

    # initializes tree
    def __init__(self):
        self.root = Node()
        self.count = 0

    # returns True if string is present in tree, False otherwise
    def __contains__(self, string):
        return search(string)

    # inserts string in tree if not currently present
    def insert(self, string):
        head = string[0]

        self.count += 1

    # returns True if string is present in tree, False otherwise
    def search(self, string):
        pass

    # deletes given string from tree if present
    def delete(self, string):
        pass
