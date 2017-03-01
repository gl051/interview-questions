#!/usr/bin/python

"""
    Problem: given the head of a linked list, find the last N elements
    Solution: the trick is using two pointers to build a window of N elements
    and move that window until you reach the end of the list.
"""

# added a symbolic link, datastructures, pointing to the data-structures folder
# in my file system.
from datastructures import LinkedList
import random

def find_last_N(alist, n):
    if n == 0:
        print 'Wrong parameter provided, you asked to find 0 element'
        return
    first_node = alist.head
    last_node = alist.head
    # build a window spaced N
    for i in range(1, n):
        if last_node.next is None:
            print 'There are only {} in the list'.format(i)
            print alist
            return
        else:
            last_node = last_node.next
    # Move both pointers until we get to the end of the list
    while last_node.next is not None:
        last_node = last_node.next
        first_node = first_node.next
    # print N values found
    print 'Last {} elements in the list: '.format(n),
    for i in range(1, n+1):
        print first_node.value,
        first_node = first_node.next



# Build a list with 10 elements for testing
ll = LinkedList()
for i in range(1, 21):
    ll.insert(random.randint(1,100))
print 'Given list:',
print ll
find_last_N(ll, 1)
