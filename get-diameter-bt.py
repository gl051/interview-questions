"""
    Problem: calculate the diameter of a binary tree
    The diameter is the longest path between any two nodes in the tree, the path
    may or may not go through the root.
    Solution:
    diameter = max(diameter left, diameter right, max path through the root)
"""

# Make use of the binary tree defined in my datastructure, but
# note that the problem does not ask for a binary search tree,
# but only a binary tree
from datastructures import bst

def get_diameter(node):
    """
        diameter = longest path in the tree, one of the following case
        1. max path from the root
        2. diameter from left child
        3. diameter from right child
    """
    if node is None:
        return 0
    else:
        diameter_root = get_max_path(node.left) + get_max_path(node.right) + 1
        #print 'max_path from {} is {}'.format(node.value, diameter_root)
        diameter_left = get_diameter(node.left)
        diameter_right = get_diameter(node.right)
        return max(diameter_left, diameter_right, diameter_root)

def get_max_path(node):
    # get the max path starting from that node
    if node is None:
        return 0
    else:
        max_left =  get_max_path(node.left)
        max_right = get_max_path(node.right)
        return 1 + max(max_right, max_left)

def get_diameter2(node):
    # we return a tuple (height, diameter)
    if node is None:
        return (0, 0)
    else:
        leftRes = get_diameter2(node.left)
        rightRes = get_diameter2(node.right)
        node_height = max(leftRes[0], rightRes[0]) + 1
        leftDiam = leftRes[1]
        rightDiam = rightRes[1]
        node_root_diam = leftRes[0] + rightRes[0] + 1
        node_diam = max(leftDiam, rightDiam, node_root_diam)
        return (node_height, node_diam)


bt = bst.Tree()
bt.insert(100)
bt.insert(50)
bt.insert(30)
bt.insert(140)
bt.insert(60)
bt.insert(70)
bt.insert(80)
bt.insert(20)
bt.insert(10)
bt.insert(1)

#bt.show()
print get_diameter(bt.root)
print get_diameter2(bt.root)
