import pytest
import count_letters


@pytest.mark.parametrize("input_string, result",[
    ("Hello", 5),
    ("Hello 456 !", 5),
    ("345.456.555 is like 100-3--,8", 6)
    ])
def test_count_letters(input_string, result):
    assert count_letters.count_letters(input_string) == result

@pytest.mark.parametrize("input_string, result",[
    ("Hello", 5),
    ("Hello 456 !", 5),
    ("345.456.555 is like 100-3--,8", 6)
    ])
def test_count_letters_using_collection(input_string, result):
    assert count_letters.count_letters_using_collection(input_string) == result
