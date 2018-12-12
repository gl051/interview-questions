import find_duplicates


def test_solution_1():
    input_array = [7, 89, 89, 10, 9, 1, 7, 40]
    assert(find_duplicates.solution1(input_array) == set([89, 7]))


def test_solution_1_empty_list():
    input_array = []
    assert(find_duplicates.solution1(input_array) == set())


def test_solution_1_all_duplicates():
    input_array = [3, 3, 3, 3, 3, 3]
    assert(find_duplicates.solution1(input_array) == set([3]))


def test_solution_2():
    input_array = [7, 89, 89, 10, 9, 1, 7, 40]
    assert(find_duplicates.solution2(input_array) == set([89, 7]))


def test_solution_2_empty_list():
    input_array = []
    assert(find_duplicates.solution2(input_array) == set())


def test_solution_2_all_duplicates():
    input_array = [3, 3, 3, 3, 3, 3]
    assert(find_duplicates.solution2(input_array) == set([3]))
