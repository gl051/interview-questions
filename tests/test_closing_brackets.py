import pytest
import closing_brackets


@pytest.mark.parametrize("input_string, result",[
    ("", True),
    ("This is a test (to validate correct result)", True),
    ("(()", False),
    ("Go here ( and there ( hello, hello) bye bye)", True),
    ("Go here ( and there ( hello, hello) bye bye) and one more to break it )", False),
    ("Mix [( one, two ()]", False),
    ("[[[[(()]]]", False),
    ("{{{ and [[ this ( or) ]] close }}} end", True)
    ])
def test_check_closure_using_stack(input_string, result):
    assert(closing_brackets.check_closure_using_stack(input_string) == result)

