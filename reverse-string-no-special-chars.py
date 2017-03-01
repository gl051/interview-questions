#!/usr/bin/python

"""
Problem: http://www.geeksforgeeks.org/reverse-an-array-without-affecting-special-characters/
"""

def reverse(astring):
    q = []
    chars = list(astring)
    if astring is None or len(astring) == 1:
        return astring
    else:
        for pos, c in enumerate(chars, 0):
            if c.isalpha():
                q.append(c)
                chars[pos] = None
        for pos, c in enumerate(chars, 0):
            if c is None:
                chars[pos] = q.pop()
        return ''.join(chars)

def reverse2(astring):
    chars = list(astring)
    pos_forward = 0
    pos_bacward = len(chars) - 1
    while pos_forward < pos_bacward:
        if chars[pos_forward].isalpha() is False:
            pos_forward += 1
            continue
        if chars[pos_bacward].isalpha() is False:
            pos_bacward -= 1
            continue
        chars[pos_forward], chars[pos_bacward] = chars[pos_bacward], chars[pos_forward]
        pos_forward += 1
        pos_bacward -= 1
    return ''.join(chars)



print reverse2("abcd")
print reverse("a,b^cd&fg")
print reverse2("a,b^cd&fg")
