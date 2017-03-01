#!/usr/bin/python

"""
    Problem: get the depth of a node of a given bst
    Solution: you calculate_depth the node and count how many depth you have crossed
    It is a O(logN) time complexity
"""

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Global variable to count the depth
depth = -1

def calculate_depth(head, value):
    global depth
    # It's a global variale, set to 0 at the beginning or you will keep
    # the value for multiple calls to the function
    depth = 0
    if head is None:
        return -2
    else:
        return __calculate_depth(head, value)

    #return depth

def __calculate_depth(node, value):
    global depth
    if node.value == value:
        return depth
    else:
        if value < node.value and node.left is not None:
            depth = depth + 1
            return __calculate_depth(node.left, value)
        elif value > node.value and node.right is not None:
            depth = depth + 1
            return __calculate_depth(node.right, value)
        else:
            # Got to the end of the tree and didn't fine the ndoe
            return -1

# Testing
head = Node(100)
n1 = Node(50)
n2 = Node(150)
head.left = n1
head.right = n2
n3 = Node(20)
n1.left = n3
n4 = Node(6)
n3.left = n4
print 'depth of {0} = {1}'.format(150, calculate_depth(head, 150))
print 'depth of {0} = {1}'.format(20, calculate_depth(head, 20))
print 'depth of {0} = {1}'.format(6, calculate_depth(head, 6))
print 'depth of {0} = {1}'.format(100, calculate_depth(head, 100))
print 'depth of {0} = {1}'.format(500, calculate_depth(head, 500))
