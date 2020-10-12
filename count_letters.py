"""
    GIVEN a string 
    THEN return the count of all the letters of the alphabet that it contains
"""

import collections

def count_letters(astring):
    counter = 0
    for c in astring.lower():
        if c.isalpha():
            counter = counter + 1
    return counter

def count_letters_using_collection(astring):
    counter = collections.Counter(astring.lower())
    # we iter the dictionary and get only count for alpha key,
    # then we sum the individual count
    return sum([(v) for (k,v) in counter.items() if k.isalpha()])
