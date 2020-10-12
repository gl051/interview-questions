"""
    Given a sorted list of integer
    And a desired value to look for
    Then implement a binary search to return the position of the element 
    Or -1 if the value has been not found
"""

CODE_VALUE_NOT_FOUND = -1

def binary_search(lst, value):
    if lst is None:
        return CODE_VALUE_NOT_FOUND
    else:
        return __binary_search(lst, value)

def __binary_search(lst, value):
    # when we reached an empty list it means
    # the record has not been found.
    if len(lst) == 0:
        return CODE_VALUE_NOT_FOUND

    # get the middle position
    middle = int(len(lst) / 2)
    # lucky, we found the value, return it!
    if value == lst[middle]:
        return middle
    # keep serching on the right
    if value > lst[middle]:
        return __binary_search(lst[middle+1:], value)
    # keep searching on the left
    if value < lst[middle]:
        return __binary_search(lst[:middle], value)
