# Given an array of integer find the duplicates and print them


def solution1(input):
    duplicates = []
    sarray = sorted(input)
    end = len(input) - 1
    for pos, val in enumerate(sarray):
        if pos < end and val == sarray[pos+1]:
            duplicates.append(val)
    return set(duplicates)


def solution2(input):
    # Create a list of only duplicates and get the set
    return set([x for x in input if input.count(x) > 1])
