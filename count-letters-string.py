#!/usr/bin/env python

"""
    Problem: given a string count only the letters it contains
"""

import collections

def count_letters(astring):
    alphabet = ['a', 'b']
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


s = "ciao 33 gatti in Centro!"
print count_letters(s)
print count_letters_using_collection(s)
