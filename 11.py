#!/usr/bin/env python3

import numpy as np

SERIAL = 7347
SZ = 300

xx, yy = np.meshgrid(range(1,1+SZ), range(1,1+SZ))
rackid = xx + 10
powlev = rackid * yy + SERIAL
powlev *= rackid
powlev //= 100
powlev %= 10
powlev -= 5

def print_5x5(a, x, y):
    print(a[x-2:x+3,y-2:y+3])

def max_power(square_size):
    maxpowsz = SZ - square_size + 1
    maxpow = np.zeros((maxpowsz, maxpowsz), dtype=int)
    for y in range(maxpowsz):
        for x in range(maxpowsz):
            maxpow[y,x] = np.sum(powlev[y:y+square_size,x:x+square_size])
    maxpos = np.unravel_index(np.argmax(maxpow), maxpow.shape)
    maxpowval = maxpow[maxpos]
    return np.array(maxpos) + 1, maxpowval

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
