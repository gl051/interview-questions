#!/usr/bin/env python

"""
    Problem:
    Given a binary tree check if it is a binary search tree.

    Solution:
    Binary search tree implies that:
    - the left subtree of a a node contains only nodes less than itself
    - the right subtree of a node contains only nodes greater/equals than itself
    - both left and right subtrees are binary search trees
    Using an in order traversal, if this is a  binary tree you will get an array of
    ordered nodes, if not it means is not a binary tree. 

"""

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Two global variables to control,
# previous value to avoid saving traversal in an array
# keep_looking to stop the recursion as soon as we find is not a bst
prev_value = None
keep_looking = True

def inorder_check(head):
    if head is None:
        return True
    else:
        __inorder_check(head)

def __inorder_check(head):
    global prev_value
    global keep_looking

    # To stop the recursion you add the logic check of keep_looking at
    # any step of the recursion: left, center, right

    # Go left
    if head.left is not None and keep_looking:
        __inorder_check(head.left)
    # Go center
    if keep_looking:
        print head.value
        if head.value >= prev_value:
            prev_value = head.value
        else:
            print 'this is not a bst!'
            keep_looking = False;
            return
    # Go right
    if head.right is not None and keep_looking:
        __inorder_check(head.right)

# Testing
head = Node(100)
n1 = Node(50)
n2 = Node(150)
head.left = n1
head.right = n2
n3 = Node(20)
n1.left = n3
n4 = Node(60)
n3.left = n4
inorder_check(head)
