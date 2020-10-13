import pytest
import count_substrings

@pytest.mark.parametrize("input_string, pattern, result", 
    [
        ("car is a car", "car", 2),
        ("this is a car, and this is a car, got it", "car", 2),
        ("we drove with our car and we went home", "car", 1)
    ]
)
def test_count_substring(input_string, pattern, result):
    assert count_substrings.count_substring(input_string, pattern) == result 
