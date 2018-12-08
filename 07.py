#!/usr/bin/env python3
from collections import defaultdict

fwd = defaultdict(list)
back = defaultdict(list)

with open('07.txt') as f:
    for line in f:
        if not line.strip():
            break
        l = line.split()
        step_before, step = l[1], l[7]
        fwd[step_before].append(step)
        back[step].append(step_before)


candidates = [x for x in fwd if x not in back]

while candidates:
    candidates.sort()
    curr = candidates.pop(0)
    print(curr, end='')
    # Iterate over steps that depends on the finished step and check if all
    # their deps are finished
    for s in fwd[curr]:
        back[s].remove(curr)
        if not back[s]:
            candidates.append(s)
