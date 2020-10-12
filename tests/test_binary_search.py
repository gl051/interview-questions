import pytest 
import binary_search

def test_binary_search_1():
    assert binary_search.binary_search([10, 23, 56, 78, 200], 56) == 2

def test_binary_search_2():
    assert binary_search.binary_search([], 56) == binary_search.CODE_VALUE_NOT_FOUND

def test_binary_search_3():
    assert binary_search.binary_search([10, 23, 56, 78, 200, 500, 600, 670, 891], 10) == 0

def test_binary_search_4():
    assert binary_search.binary_search([10, 23, 56, 78, 200, 500, 600, 670, 891], 11) == binary_search.CODE_VALUE_NOT_FOUND

def test_binary_search_5():
    assert binary_search.binary_search([10], 10) == 0

def test_binary_search_6():
    assert binary_search.binary_search([10], 5) == binary_search.CODE_VALUE_NOT_FOUND
