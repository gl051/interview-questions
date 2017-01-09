"""
 Question: Given the head of a linked list, reverse it. Head could be None
 as well for empty list.

 Input:
 None
 1 --> 2 --> 3 --> None

 Output:
 None
 None --> 3 --> 2 --> 1
"""

class Node(object):
	def __init__(self, data=None, next_node=None):
		self.data = data
		self.next = next_node

	def str(self):
		print 'node val:{0}'.format(self.data)

def reverse_1(head):
    """
        This solution does not require additional data structures.
        It traverses the list and adjust the references to the nodes.
    """
    current = head               # the current node to process
    previous = None              # before the current
    while current:               # until we do not reach the end of the list
        nextone = current.next   # we need a reference to/save the current.next
        current.next = previous  # we have currrent.next saved, shift references now
        previous = current       # for the next iteration
        current = nextone        # move ahead of one node
    return previous              # at the end the previoud one is the tail of the original list


def reverse_2(head):
    """
        This solution consider the input list as an immutable object, indeed
        it works on creating a new list starting from the one in input
    """
    current = head
    previous = None
    while current:
        node = Node(current.data, previous)
        previous = node
        current = current.next
    return previous

def print_me(head):
    if head is None:
        print ''
        return
    else:
        print head.data,
        print_me(head.next)

prev_node = None
for i in range(10, 0, -1):
    new_node = Node(i, prev_node)
    prev_node = new_node

"""
    Testing the implementation
    Note:
    - reverse_1 does not use additional space in memory
    - reverse_2 treats the list as immutable object (create a new one reversed)
"""
head = prev_node
print 'Input:'
print_me(head)
n = reverse_2(head)
print 'Reversed:'
print_me(n)
print 'Original:'
print_me(head)
