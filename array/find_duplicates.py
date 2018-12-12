# Given an array of integer find the duplicates and print them

from random import randint


def solution(input):
    duplicates = []
    sarray = sorted(input)
    end = len(input) - 1
    for pos, val in enumerate(sarray):
        print(pos, val)
        if pos < end and val == sarray[pos+1]:
            duplicates.append(val)
    return duplicates


def solution2(input):
    # Create a list of only duplicates and get the set
    return set([x for x in input if input.count(x) > 1])


def array_generator(length):
    return [randint(1, 10) for x in range(length)]


a = [10, 5, 90, 5, 8, 90, 1, 4]
print("Given {}, duplicates are {}".format(a, solution(a)))
