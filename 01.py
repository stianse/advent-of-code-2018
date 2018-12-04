#!/usr/bin/env python3
from itertools import cycle

with open('01.txt') as f:
    inputs = f.read().splitlines()

changes = list(map(int, inputs))

# Part 1
print(sum(changes))

# Part 2
freq = 0
seen = {0}
it = cycle(changes)
while True:
    freq += next(it)
    if freq in seen:
        break
    seen.add(freq)
print(freq)
