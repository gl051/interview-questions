#!/usr/bin/python

"""
     Problem: https://www.hackerearth.com/problem/algorithm/substrings-count-3/
"""
filename = "input.txt"
words = []
N = -1
Q = 1000000
with open(filename,'r') as fin:
    # read from the input file in order: N value, the N words and
    # the Q value and then per each Q val search substring
    for count_line, line in enumerate(fin, 0):
        if count_line == 0:
            N = int(line)
            words.append('dummy entry')
        elif count_line < N + 1:
            words.append(line.strip())
        elif count_line == N+1:
            Q = int(line)
        elif count_line > N + 1:
            # get the substring and boundaries to search in the N list
            L, R, str = line.strip().split()
            L = int(L)
            R = int(R)
            count_match = 0
            # per each Q val, search how many matches we have
            for i in range(L, R+1):
                if str in words[i]:
                    count_match = count_match + 1
            if count_match > 0:
                print count_match
