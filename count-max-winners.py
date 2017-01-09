"""
    Problem: https://www.hackerearth.com/problem/algorithm/tournament-easy/
"""
# we use the Python HEAP module
import heapq

filename = "input.txt"
# heap repr
h = []
# all players in the file
all = []
with open(filename,'r') as fin:
    for count_line, line in enumerate(fin, 0):
        if count_line == 0:
            continue
        first_player, second_player = line.strip().split()
        all.append(first_player)
        all.append(second_player)
# we sort the all players O(NlogN)
all.sort()
# traverse the list O(N), count of player's name represents how many times he won
prev_player = None
count_win = 0
for p in all:
    if p == prev_player:
        count_win = count_win + 1
    else:
        # push in the heap the tuple (count, player), order is important because
        # is the first element of the tuple that is used for sorting
        heapq.heappush(h, (count_win, prev_player))
        count_win = 0
    prev_player = p
# print the heap, last element most succesfull player 
print h
