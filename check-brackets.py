#!/usr/bin/env python

"""
    Given an assigned string, check if all the brackets are paired correctly.
    For example:
    - {{}}{{}} ---> True
    - {{} --> False

    Solution: use a stack for pushing and popping matching parenthesis while
    traversing the string.
"""

def check_brackets_simple(str):
    """
        The simple implementation assumes only one bracket type, i.e. {
    """
    stack = []
    for c in str:
        if c == '{':
            stack.append(c)
        if c == '}':
            if len(stack) > 0:
                stack.pop()
            else:
                #print 'Found } without a previous {, syntax error'
                return False
    return True if len(stack) == 0 else False

def check_brackets_complex(str):
    """
        The complex version assume different bracket types. i.e. {, [
        - [{}] --> True
        - [{]} --> False
    """
    matching = {'}':'{', ']':'['}
    stack = []
    for c in str:
        if c in ['{','[']:
            stack.append(c)
        if c in ['}', ']']:
            if len(stack) > 0:
                last_inserted = stack.pop()
                if matching[c] != last_inserted:
                    #'this bracket is not the same type as the last opened'
                    return False
            else:
                #print 'Found closing brackets without a previous open,syntax error'
                return False
    return True if len(stack) == 0 else False

def check_brackets_optimized(str):
    """
        It uses only a counter instead of a stack to save on memory usage.
        This is equivalent of check_brackets_simple
    """
    counter = 0
    for c in str:
        if c == '{':
            counter = counter + 1
        if c == '}':
            if counter > 0:
                counter = counter - 1
            else:
                #print 'Found } without a previous {, syntax error'
                return False
    return True if counter == 0 else False
