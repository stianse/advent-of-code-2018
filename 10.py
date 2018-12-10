#!/usr/bin/env python3
import numpy as np
import re

P = []
V = []
with open('10.txt') as f:
    for line in f:
        x0, y0, vx, vy = re.findall('-?\d+', line.strip())
        P.append((x0, y0))
        V.append((vx, vy))

P = np.array(P, dtype=int)
V = np.array(V, dtype=int)

best_dist = None
best_sec = None
sec = 0
while True:
    p = P + V * sec
    min_ = np.min(p, axis=0)
    max_ = np.max(p, axis=0)
    dist = np.sum(max_ - min_)
    if best_dist is None or dist < best_dist:
        # This isn't necessarily this the correct answer, but it's very likely.
        best_sec = sec
        best_dist = dist
    if dist > best_dist:
        break
    sec += 1


def print_points(p):
    minx, miny = np.min(p, axis=0)
    maxx, maxy = np.max(p, axis=0)
    sx = maxx - minx + 1
    sy = maxy - miny + 1

    a = [['.'] * sx for _ in range(sy)]
    for x, y in p:
        a[y-miny][x-minx] = '#'
    for row in a:
        print(''.join(row))

for sec in range(best_sec-1, best_sec+2):
    print('\n', sec, 'seconds')
    print_points(P + sec * V)
