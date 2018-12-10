#!/usr/bin/env python3
from collections import Counter

with open('02.txt') as f:
    inputs = f.read().splitlines()

# Part 1
count_two = 0
count_three = 0
for line in inputs:
    letter_count = Counter(line).values()
    if 2 in letter_count:
        count_two += 1
    if 3 in letter_count:
        count_three += 1

print(count_two, '*', count_three, '=', count_two * count_three)

# Part 2
def distance(s1, s2):
    assert len(s1) == len(s2)
    dist = 0
    for a, b in zip(s1, s2):
        if a != b:
            dist += 1
    return dist

def commonstr(s1, s2):
    assert len(s1) == len(s2)
    common = ''
    for a, b in zip(s1, s2):
        if a == b:
            common += a
    return common

for line1 in inputs:
    for line2 in inputs:
        dist = distance(line1, line2)
        if dist == 1:
            common = commonstr(line1, line2)
            print(line1, line2, common)
