#!/usr/bin/env python3
import numpy as np
import re

pattern = re.compile(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)')

with open('03.txt') as infile:
    inputs = infile.read().splitlines()

# Part 1
counts = np.zeros([1000, 1000], dtype=int)
for line in inputs:
    m = pattern.match(line)
    i, x, y, w, h = [int(x) for x in m.groups()]
    counts[y:y+h, x:x+w] += 1

print('Squares overlapping', np.sum((counts > 1)))

# Part2
for line in inputs:
    m = pattern.match(line)
    i, x, y, w, h = [int(x) for x in m.groups()]
    if np.all(counts[y:y+h, x:x+w] == 1):
        print('Non-overlapping id', i)
