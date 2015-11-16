# Implementation of an AVL balanced tree data structure
# By: Jacob Rockland

from binary_search_tree import BinarySearchTree, Node

# implementation of AVL node
class AVLNode(Node):

    def __init__(self, data):
        self.key = key
        if data is None:
            self.data = key
        else:
            self.data = data
        self.left_child = None
        self.right_child = None
        self.parent = None
        self.balance_factor = 0


# implementation of AVL tree
class AVLTree(BinarySearchTree):

    # update the balance factor for a given node
    def update_balance_factor(self, node):
        node.balance_factor = self.height(node.left_child) - self.height(node.right_child)

    # returns True if a given node is balanced, False otherwise
    def is_balanced(self, node):
        return -1 <= node.balance_factor <= 1

    # performs a right-rotate on the given node, returning new root node
    def right_rotate(self, node):
        """
         D         B
        /    ==>    \
       B             D
        \           /
         C         C

        """
        d_node = node

        b_node = d_node.left_child # must exist
        c_node = b_node.right_child # musn't exist

        b_node.right_child = d_node
        d_node.left_child = c_node

        return b_node

    # performs a left-rotate on the given node, returning new root node
    def left_rotate(self, node):
        """
         B             D
          \    ==>    /
           D         B
          /           \
         C             C

        """
        b_node = node

        d_node = d_node.right_child # must exist
        c_node = b_node.left_child # musn't exist

        d_node.left_child = b_node
        b_node.right_child = c_node

        return d_node

    # inserts a data item into the tree, O(log(n))
    def insert(self, data):
        pass # FIXME: Implement me!

    # removes the first found item in the tree with matching data, O(log(n))
    def remove(self, data):
        pass # FIXME: Implement me!
