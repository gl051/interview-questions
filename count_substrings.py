"""
    Given a string and a substing
    Then find all the occurences of the substring in the string

    Input: dhimanman, man
    Output: 2
"""


def count_substring(input_string, pattern):
    if input_string is None or len(input_string) == 0 or pattern is None or len(pattern) == 0:
        return None 
    tokens = input_string.split(pattern)
    return len(tokens) - 1
