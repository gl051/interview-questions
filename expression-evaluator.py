#!/usr/bin/python

"""
    Author: Gianluca Biccari

    Problem (sy):
    Implement an expression evaluator, with the following requirements:
    A function that accepts an expression string (e.g. "1+6/3-2*8") and returns
    a numerical result (e.g. -13). The expression string will contain only numbers
    (1 or more digits each) and operators (+, -, /, *)
    Bonus points: write a function to evaluate expressions that may contain parentheses
"""
import re

def evaluate_expression(astr):
    """
        This evaluate a string expression with no parentheses,
        it works using a stack to evaluate first * and / operations.
    """
    values = []
    operators = []
    # tokenize string with regular expression
    tokens = re.split('([+-/*]|\d+)', astr)
    # clear from the empty tokens
    tokens = [i for i in tokens if i]
    # execute all * and / operation first,
    # use a stack to keep all tokens and get
    # back the first operand when you see a * or /
    stack = []
    i = 0
    # need to use a while loop to move forward i inside
    while i < len(tokens):
        #print 'stack: ', stack
        tk = tokens[i]
        #print "i:{}, tk:{}".format(i, tk)
        if tk not in ['*', '/']:
            stack.append(tk)
        else:
            # we have a * or /, we pop the stack to get the first operand,
            # then we move to the next token to get the second operand.
            # we evaluate * or / and we push in the stack the result.
            prev = stack.pop()
            i += 1
            succ = tokens[i]
            prev = int(prev)
            # consider if the operand is negative value
            # i.e. 3*-2 = -6
            if succ is '-':
                i += 1
                succ = tokens[i]
                succ = int(succ)*(-1)
            else:
                succ = int(succ)
            if tk is '*':
                stack.append(prev*succ)
            elif tk is '/':
                stack.append(prev/succ)
        i += 1
    # Go through the list to execute + and - operations,
    # iterate the list and start building the sum with the right sign
    op = '+'
    tot = 0
    for v in stack:
        if v in ['+', '-']:
            op = v
            continue
        else:
            if op is '+':
                tot += int(v)
            elif op is '-':
                tot -= int(v)
    return tot

def evaluate_complex_expression(astr):
    """
        This method evaluates a string expression with parentheses, also nested.
        We assume that all parentheses are properly closed.
        This code is an evolution of the method above and use its logic on the
        sub-expression enclosed in parentheses.
        We use again a stack to extract the substrings and put back later their
        evaluation.
    """
    print 'Evaluate: ', astr
    # tokenize string with regular expression
    tokens = re.split('([+-/*)()]|\d+)', astr)
    # clear from the empty tokens
    tokens = [i for i in tokens if i]
    stack = []
    # process the operation inside parentheses
    for tk in tokens:
        if tk is ')':
            cache = []
            val = ''
            while val is not '(':
                val = stack.pop()
                cache.append(val)
            cache.pop()
            cache.reverse()
            # I rebuild a string just because I want to reused the first method
            val = evaluate_expression(''.join(cache))
            stack.append(str(val))
        else:
            stack.append(tk)
    return evaluate_expression(''.join(stack))

# Demoing:
print evaluate_complex_expression("1+3*(4-2)")
print evaluate_complex_expression("1+3*4-2")
