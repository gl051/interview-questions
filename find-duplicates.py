"""
    Problem: given an array of integers, find all elements where in a range
    of indexes, i and j, where i - j < D, where A[i] - A[j] < T
"""

def find_duplicates_simple_first(alist, T):
    """
        Simplified the problem excluding the check on the indexes to help
        thinking a  different approach that looping twice the arrray
    """
    # sort array first, it will take N log N
    alist.sort()
    # iterate through the array once, it will take N
    for i in range(1, len(alist)):
        if abs(alist[i]-alist[i-1]) <= T:
            print abs(alist[i]-alist[i-1])
            print 'Found similars: {}, {}'.format(alist[i-1], alist[i])
            return True
    return False

def find_duplicates(alist, T, D):
    """
        Starting from the simplified example, I just need to check also the
        position of the two elements I am comparing. To do that I need to bring
        with me, in the sorted array, the original index.
    """
    # create array with (val,pos)
    a = [(i[1], i[0]) for i in enumerate(l)]
    # sort by val (lucky for us default look at the first element of the tuple)
    # best sorting array are O(NlogN)
    a.sort()
    # traverse the array only one O(N), and compare both value and original distances
    for i in range (1, len(a)):
        if abs(a[i][0]-a[i-1][0]) <= T and abs(a[i][1]-a[i-1][1]) < D :
            return True


l = [10, 20, 5, 15, 7, 40, 0]
print find_duplicates(l, 2, 3)
