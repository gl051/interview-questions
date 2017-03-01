#!/usr/bin/python

"""
    Problem: given a binary tree and two nodes, find the lowest common ancestor.
    You can assume that the two nodes exist in the tree.

    Tree:
              20
          8        22
      4       12
           10    14

    (4, 14) --> 8
    (8, 22) --> 20
    (4, 22) --> 20
    (8, 14) --> 8

    Solution: using the property tree we know that the lowest common ancestor is
    when the two values split travesing down the tree
"""

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def search_ancestor(head, value1, value2):
    global ancestor
    ancestor = None
    if head is None:
        return None
    else:
        n = __search_anchestor(head, value1, value2)
        if n is None:
            print 'Not found ancestor'
        else:
            print 'Anchestor value for ({0}, {1}) is {2}'.format(value1, value2, n.value)


def __search_anchestor(node, value1, value2):
    # if both values are less, keep searching left
    if (value1 < node.value) and (value2 < node.value):
        if node.left is not None:
            return __search_anchestor(node.left, value1, value2)
    # if both values are greater, keep searching right
    elif (value1 > node.value) and (value2 > node.value):
        if node.right is not None:
            return __search_anchestor(node.right, value1, value2)
    # if values split directions this is the lowest anchestor
    else:
        return node

# Testing
head = Node(20)
n1 = Node(8)
n2 = Node(22)
head.left = n1
head.right = n2
n3 = Node(4)
n1.left = n3
n4 = Node(12)
n2.right = n4
n5 = Node(10)
n4.left = n5
n5 = Node(14)
n4.right = n5
search_ancestor(head, 4, 14)
search_ancestor(head, 8, 22)
search_ancestor(head, 4, 22)
search_ancestor(head, 8, 14)
