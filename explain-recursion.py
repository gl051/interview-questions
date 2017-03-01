#!/usr/bin/python

"""
    Problem: use recursion to find the position of an element in a list
"""

def find_position(alist, value):
    global position
    position = -1
    if alist is None:
        print 'List is None'
    else:
        return __find_position(alist, value)

# You use a global variable to hold where you are in traversing the list,
# an alternative is to provide a third parameter to keep this information
position = 0
def __find_position(lst, value):
    global position
    position = position + 1
    # condition to exit successfully from the recursion
    if lst[position] == value:
        return position
    else:
        # if the next position is stil in the list, call recursion again
        if position + 1 < len(lst):
            return __find_position(lst, value)
        else:
            # element not found in the array, exit not successfully
            return -1

mylist = [12, 45, 56, 67, 89]
print mylist
print 'Position of {0}: {1}'.format(12, find_position(mylist, 12))
print 'Position of {0}: {1}'.format(89, find_position(mylist, 89))
print 'Position of {0}: {1}'.format(56, find_position(mylist, 56))
print 'Position of {0}: {1}'.format(100, find_position(mylist, 100))
