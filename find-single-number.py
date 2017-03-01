#!/usr/bin/python

"""
    Problem: Given an array of integers, every element appears twice
    except for one. Find that single one. Your algorithm should have a linear
    runtime complexity.
"""

def find_single(alist):
    """
        It the elemens can appear only twice or one, you can use
        an hash table to toggle what you see when iterating the array.
        This approach would not work if an element appear and odd times.
    """
    ht = {}
    for i in alist:
        if ht.has_key(i):
            ht.pop(i)
        else:
            ht[i] = 'check'
    print ht.keys()

def find_single_2(alist):
    """
        We sort the list and look per each element if the one before and the one
        after is different, this means is single element. We need to check separate
        first and last element of the list, since we use a tre pointer window.
        Run time complexity assuming the sorting is done in O(NlogN), will be in total
        equals to O(NlongN + N) -> NlogN.
        Plus, everthing is done in place
    """
    # sort the list
    alist.sort()
    # check first element
    if alist[0] != alist[1]:
        print alist[0],
    # check element in the middle, verify on val before and val aftert
    for idx_middle in range(1,len(alist)-1):
        if (alist[idx_middle] != alist[idx_middle-1]) and (alist[idx_middle] != alist[idx_middle+1]):
            print alist[idx_middle]
    # check last element
    if alist[-1] != alist[-2]:
        print alist[-1],

find_single_2([23, 45, 23, 10, 10])
