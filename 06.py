#!/usr/bin/env python3
import numpy as np
import re

coords = []
with open('06.txt') as f:
    for line in f:
        c = [int(x) for x in line.split(', ')]
        coords.append(c)

# Part 1
xmax, ymax = np.array(coords).max(axis=0) + 1
best_coord = np.empty((ymax, xmax), dtype=int)
best_dist = np.ones((ymax, xmax), dtype=int) * (xmax + ymax + 1)

for y in range(ymax):
    for x in range(xmax):
        for idx, (cx, cy) in enumerate(coords):
            dist = abs(y - cy) + abs(x - cx)
            if dist < best_dist[y, x]:
                best_dist[y, x] = dist
                best_coord[y, x] = idx
            elif dist == best_dist[y, x]:
                best_coord[y, x] = -1

# Get values on the border. These groups are considered to have infinite distance
inf = np.unique(np.concatenate((
    best_coord[:,0],
    best_coord[:,-1],
    best_coord[0,:],
    best_coord[-1,:])))

best_idx = None
best_count = -1
unique, counts = np.unique(best_coord, return_counts=True)
for idx, c in zip(unique, counts):
    if idx in inf:
        continue
    if c > best_count:
        best_idx = idx
        best_count = c

print(best_idx, best_count)

# Part 2

safe = np.zeros((ymax, xmax), dtype=int)

for y in range(ymax):
    for x in range(xmax):
        dist_sum = 0
        for cx, cy in coords:
            dist_sum += abs(y - cy) + abs(x - cx)
        if dist_sum < 10000:
            safe[y, x] = 1

print(np.sum(safe))
