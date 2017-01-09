"""
    Problem: search an element in a sorted array that has been rotated around
    a pivot value unkown to you.
    sorted array: 1, 2, 3, 4, 5
    rotated array given: 3, 4, 5, 1, 2
    http://www.geeksforgeeks.org/search-an-element-in-a-sorted-and-pivoted-array/
"""


def find_element(alist, val):
    """
        We run a binary search to obtain log N computation cost, we need
        to identify where to search for the element since there will be half
        array sorted and half array not sorted. Check if the val to search is
        in the half sorted otherwise look in the other half.
    """
    print alist, val
    if len(alist) == 0:
        return
    middle = len(alist)/2
    mv = alist[middle]
    last = alist[-1]
    first = alist[0]
    if mv == val:
        return mv
    else:
        # if it's one element only end since there is not paritioning
        if len(alist) == 1:
            return
        # detect sorted half and unsorted half
        if first < mv:
            sorted_half = alist[0:middle]
            unsorted_half = alist[middle+1:]
        else:
            sorted_half = alist[middle+1:]
            unsorted_half = alist[0:middle]
        # depending if val is in sorted half or not call the right recursion
        if sorted_half[0] <= val <= sorted_half[-1]:
            return find_element(sorted_half,val)
        else:
            return find_element(unsorted_half,val)


l = [1, 2, 3, 4, 5]
print find_element(l, 5)
