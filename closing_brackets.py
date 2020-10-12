"""
    Given an assigned input_stringing
    And that we can have both `(` and `{` brackets 
    Then check if all the brackets are paired correctly.

    For example:
    - {{}}{{}} ---> True
    - {{} --> False
    - {((()))} --> True
    - {())} --> False

"""

def check_closure_using_stack(input_string):
    # dict where 'opening bracket': 'closing bracket'
    matches = {
        '(': ')',
        '[': ']', 
        '{': '}'
    }
    stack = []
    for c in input_string:
        # opening bracket found
        if c in matches.keys():
            stack.append(c)
        # closing bracket found
        if c in matches.values():
            if len(stack) > 0:
                last_open_bracket = stack.pop()
                if matches[last_open_bracket] != c:
                    print(f"Found a mismatch between closing {c} and opening {last_open_bracket} brackets.")
                    return False
            else:
                print(f"Found extra closing bracket {c}")
                return False
    return True if len(stack) == 0 else False
