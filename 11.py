#!/usr/bin/env python3

import numpy as np

SERIAL = 7347
SZ = 300

xx, yy = np.meshgrid(range(1,1+SZ), range(1,1+SZ))
rackid = xx + 10
powlev = (rackid * yy + SERIAL) * rackid
powlev = (powlev // 100) % 10 - 5

# Use a summed-area table
area = powlev.cumsum(axis=0).cumsum(axis=1)
# pad so that we don't need if-tests in loop
area = np.pad(area, (1,0), 'constant')

def max_power(square_size):
    nsquares = SZ - square_size + 1
    n = nsquares + 1 # compensate for padding
    maxpow = np.zeros((n, n), dtype=int)
    for y in range(1, n):
        for x in range(1, n):
            x0, y0 = x-1, y-1
            x1, y1 = x+square_size-1, y+square_size-1
            #maxpow[y,x] = np.sum(powlev[y0:y1,x0:x1])
            maxpow[y,x] = area[y1, x1] + area[y0, x0] - area[y0, x1] - area[y1, x0]

    maxpos = np.unravel_index(np.argmax(maxpow), maxpow.shape)
    maxpowval = maxpow[maxpos]
    return maxpos, maxpowval

# Part 1
pos, val = max_power(3)
print("X,Y,val", pos[1], pos[0], val)

# Part 2
best_sqsz = None
best_power = None
for sqsz in range(1, SZ+1):
    pos, power = max_power(sqsz)
    if best_power is None or power > best_power:
        best_power = power
        best_pos = pos
        best_sqsz = sqsz
print("X,Y,size,val", best_pos[1], best_pos[0], best_sqsz, best_power)
