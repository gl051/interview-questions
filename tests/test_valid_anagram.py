import pytest
import valid_anagram


def test_is_anagram_with_hash():
    assert valid_anagram.is_anagram_with_hash("car", "rac") == True 

def test_is_anagram_with_sort():
    assert valid_anagram.is_anagram_with_sort("anagram", "nagaram") == True 
