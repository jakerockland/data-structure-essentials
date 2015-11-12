# Implementation of an AVL balanced tree data structure
# By: Jacob Rockland

from binary_search_tree import BinarySearchTree, Node

# implementation of AVL tree
class AVLTree(BinarySearchTree):

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
