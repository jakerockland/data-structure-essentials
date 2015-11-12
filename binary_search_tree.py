# Implementation of a binary search tree (BST) data structure
# By: Jacob Rockland

# node class for BST
class Node(object):

    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


# implementation of BST
class BinarySearchTree(object):

    # initializes tree
    def __init__(self, root = None):
        self.root = root

    # returns a string representation of tree
    def __repr__(self):
        return repr(self.in_order_list())

    # returns an in-order list representation of the tree
    def in_order_list(self, node = self.root):
        return [] # FIXME

    # returns an pre-order list representation of the tree
    def pre_order_list(self, node = self.root):
        return [] # FIXME

    # returns an post-order list representation of the tree
    def post_order_list(self, node = self.root):
        return [] # FIXME

    # searches for a node with the data of given key, O(log(n)) on average
    def search(self, data):
        curr = self.root
        while curr is not None:
            if curr.data == data: # node is found
                return curr
            elif curr.data < data: # searching down right subtree
                curr = curr.right_child
            elif curr.data > data: # searching down left subtree
                curr = curr.left_child
        return None # node was not found

    # inserts a data item into the tree, O(log(n)) on average
    def insert(self, data):
        node = Node(data)
        curr = self.root
        if curr is None: # tree is empty, inserting data at root
            self.root = node
        else:
            while curr is not None:
                if curr.data > data: # going down left subtree
                    if curr.left_child is None:
                        curr.left_child = node
                        return # node inserted
                    else:
                        curr = curr.left_child
                else: # going down right subtree
                    if curr.right_child is None:
                        curr.right_child = node
                        return # node inserted
                    else:
                        curr = curr.right_child

    # removes the first found item in the tree with matching data, O(log(n)) on average
    def remove(self, data, curr = self.root):
        curr = curr
        prev = None
        while curr is not None:
            if curr.data == data: # node to be removed is found
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
                    curr.data = succ.data
                    self.remove(succ.data, curr.right_child)
                return # node removed
            elif curr.data < data: # search right subtree
                prev = curr
                curr = curr.right_child
            elif curr.data > data: # search left subtree
                prev = curr
                curr = curr.left_child
        return None # node was not found
