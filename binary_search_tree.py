# Implementation of a binary search tree (BST) data structure
# By: Jacob Rockland

# node class for BST
class Node(object):

    # initializes node
    def __init__(self, key, data = None):
        self.key = key
        if data is None:
            self.data = key
        else:
            self.data = data
        self.parent = None
        self.left_child = None
        self.right_child = None

    # iterator generator for binary search tree nodes
    def __iter__(self):
       if self:
          if self.left_child is not None:
                 for node in self.left_child:
                    yield node
          yield self.data
          if self.right_child is not None:
                 for node in self.right_child:
                    yield node


# implementation of BST
class BinarySearchTree(object):

    # initializes tree
    def __init__(self, root = None):
        self.root = root
        self.size = 0

    # iterator for tree
    def __iter__(self):
        return self.root.__iter__() if self.root is not None else iter(())

    # returns length of binary tree
    def length(self):
        return self.size

    # returns length of binary tree
    def __len__(self):
        return self.size

    # returns a string representation of tree
    def __repr__(self):
        return self.in_order(self.root)

    # returns height of tree
    def height(self, node):
        if node is None:
            return -1
        height_left = self.height(node.left_child)
        height_right = self.height(node.right_child)
        return 1 + max(height_left, height_right)

    # returns an in-order string representation of the tree
    def in_order(self, node):
        if node is None:
            return ''
        return self.in_order(node.left_child) + str(node.data + ' ') + self.in_order(node.right_child)

    # returns an pre-order string representation of the tree
    def pre_order(self, node):
        if node is None:
            return ''
        return str(node.data + ' ') + self.pre_order(node.left_child) + self.pre_order(node.right_child)

    # returns an post-order string representation of the tree
    def post_order(self, node):
        if node is None:
            return ''
        return self.post_order(node.left_child) + self.post_order(node.right_child) + str(node.data + ' ')

    # searches for a node with a given key, O(log(n)) on average
    def search(self, key):
        curr = self.root
        while curr is not None:
            if curr.key == key: # node is found
                return curr
            elif curr.key < key: # searching down right subtree
                curr = curr.right_child
            elif curr.key > key: # searching down left subtree
                curr = curr.left_child
        return None # node was not found

    # returns True if list contains node with a given key, False otherwise
    def __contains__(self, key):
        return self.search(key) is not None

    # inserts a data item into the tree, O(log(n)) on average
    def insert(self, key, data = None):
        if data is None:
            data = key
        node = Node(key, data)
        curr = self.root
        if curr is None: # tree is empty, inserting data at root
            self.root = node
            self.size += 1
            return # node inserted
        else:
            while curr is not None:
                if curr.key > key: # going down left subtree
                    if curr.left_child is None:
                        curr.left_child = node
                        self.size += 1
                        return # node inserted
                    else:
                        curr = curr.left_child
                else: # going down right subtree
                    if curr.right_child is None:
                        curr.right_child = node
                        self.size += 1
                        return # node inserted
                    else:
                        curr = curr.right_child

    # removes the first found item in the tree with matching key, O(log(n)) on average
    def remove(self, key, start = None):
        if start is None:
            start = self.root
        curr = start
        prev = None
        while curr is not None:
            if curr.key == key: # node to be removed is found
                if curr.left_child is None and curr.right_child is None: # removing leaf node
                    if prev is None: # removing root
                        self.root = None
                    elif prev.left_child is curr:
                        prev.left_child = None
                    else:
                        prev.right_child = None
                elif curr.right_child is not None and curr.left_child is None: # removing node with only right child
                    if prev is None: # removing root
                        self.root = curr.right_child
                    elif prev.left_child is curr:
                        prev.left_child = curr.right_child
                    else:
                        prev.right_child = curr.right_child
                elif curr.left_child is not None and curr.right_child is None: # removing node with only left child
                    if prev is None: # removing root
                        self.root = curr.left_child
                    elif prev.left_child is curr:
                        prev.left_child = curr.left_child
                    else:
                        prev.right_child = curr.left_child
                else: # removing internal node with two children
                    succ = curr.right_child
                    while succ.left_child is not None:
                        succ = succ.left_child
                    curr.key = succ.key
                    self.remove(succ.key, curr.right_child)
                self.size -= 1
                return # node removed
            elif curr.key < key: # search right subtree
                prev = curr
                curr = curr.right_child
            elif curr.key > key: # search left subtree
                prev = curr
                curr = curr.left_child
        return None # node was not found
