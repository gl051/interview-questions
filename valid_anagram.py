"""
    Given two strings s and t
    Then write a function to determine if t is an anagram of s.

    For example:
    s = "anagram", t = "nagaram", return true.
    s = "rat", t = "car", return false.
"""

def is_anagram_with_sort(s, t):
    """
        Sort and compare the two strings. This will take the time to order
        both string and then compare them. O(NlogN)
    """
    if len(s) != len(t):
        return False
    # sort the second one and compare
    return ''.join(sorted(s)) == ''.join(sorted(t))

def is_anagram_with_hash(s, t):
    """
        Using an hash table, no sorting necessary. We iterate on the the two
        strings only, the time complexity is 2N -> N, but you need memory for
        the hash table
    """
    ht = {}
    if len(s) != len(t):
        return False
    for c in s:
        times = ht.setdefault(c, 0)
        ht[c] = times + 1
    for c in t:
        if c not in ht:
            return False
        else:
            if ht[c] > 1:
                ht[c] = ht[c] - 1
            else:
                ht.pop(c)
    return list(ht.keys()) == []

