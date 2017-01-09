"""
    Problem: return the most common words in a text file
"""
from collections import Counter
import re

input_file = "b.txt"
ct = Counter()
with open(input_file, 'r') as fread:
    for line in fread:
        #print line
        line = re.sub('[!@#$,.]', '', line)
        clean_line = line.replace('\n','').split(' ')
        ct.update(clean_line)

print ct.most_common(5)
