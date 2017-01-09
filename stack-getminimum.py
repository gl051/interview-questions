"""
    Problem:
    Design a stack which holds an integer value such that getMinimum() function
    should return the minimum element in the stack.

    Constraint: getMinimum should return the minimum value in O(1)

    For example:
    5  --> TOP
    1
    4
    6
    2

    getMinimum() should return 1, which is the minimum element in the stack.

    stack.pop()
    stack.pop()

    4  --> TOP
    6
    2

    When getMinimum() is called is should return 2 which is the minimum in the
    stack.

    Solution:
    getMinimum() O(1) let you think first to use an heap data strucutre but
    then you will have to insert and delete records as long as new values are
    pushed and popped in/from the stack. O(nlogn).
    Better use two stack the second is paried one to one with the main stack but
    keeps the current min value for that position.

    input: 2, 6, 4, 1, 5

    Main stack  Min stack
    5  -->  1
    1       1
    4       2
    6       2
    2       2
"""


class SpeciaStack(object):
    def __init__(self):
        self.__main_stack = []
        self.__min_stack = []
        self.__current_min = -1

    def is_empty(self):
        if len(self.__main_stack) == 0:
            return True
        else:
            return False

    def push(self, val):
        if self.is_empty():
            self.__current_min = val
        else:
            if val < self.__current_min:
                self.__current_min = val
        self.__main_stack.append(val)
        self.__min_stack.append(self.__current_min)

    def pop(self):
        if not self.is_empty():
            self.__main_stack.pop()
            self.__min_stack.pop()

    def get_minimum(self):
        if not self.is_empty():
            return self.__min_stack[-1]

    def __str__(self):
        return str([self.__main_stack, self.__min_stack])

# Example on how to use it:
s = SpeciaStack()
s.push(100)
s.push(5)
s.push(9)
s.push(7)
s.push(1)
print s
while not s.is_empty():
    print 'Min val is {}'.format(s.get_minimum())
    print 'pop one element'
    s.pop()
