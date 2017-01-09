"""
    Problem: Implement binary search tree on a sorted list

"""

def binary_search(lst, value):
    if lst is None:
        return -1
    else:
        return __binary_search(lst, value)

def __binary_search(lst, value):
    # when we reached an empty list it means
    # the record has not been found.
    if len(lst) == 0:
        return -1

    # get the middle position
    middle = len(lst) / 2
    # lucky, we found the value, return it!
    if value == lst[middle]:
        return value
    # keep serching on the right
    if value > lst[middle]:
        return __binary_search(lst[middle+1:], value)
    # keep searching on the left
    if value < lst[middle]:
        return __binary_search(lst[:middle], value)

l = [45, 67, 12, 78, 128]
l.sort()
print 'Input: ',    l
print 'Find {0} in the list, returns: {1}'.format(78, binary_search(l, 78))
print 'Find {0} in the list, returns: {1}'.format(12, binary_search(l, 12   ))
print 'Find {0} in the list, returns: {1}'.format(128, binary_search(l, 128))
print 'Find {0} in the list, returns: {1}'.format(1000, binary_search(l, 1000))
