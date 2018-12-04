#!/usr/bin/env python3
import numpy as np
import re

with open('04.txt') as infile:
    inputs = infile.read().splitlines()

inputs.sort()
sleep_start = None
gid = None
guards = {}
for line in inputs:
    timestr, eventstr = line.split(']')
    _, _, _, _, minute = map(int, re.findall(r'\d+', timestr))
    if 'begins shift' in eventstr:
        assert sleep_start == None
        gid = int(re.findall(r'\d+', eventstr)[0])
        if not gid in guards:
            guards[gid] = np.zeros(60, dtype=int)
    elif 'falls asleep' in eventstr:
        sleep_start = minute
    elif 'wakes up' in eventstr:
        guards[gid][sleep_start:minute] += 1
        sleep_start = None

# Part 1. The guard with most sleeping minutes
best_sum = -1
best_gid = None
for gid, counts in guards.items():
    if sum(counts) > best_sum:
        best_sum = sum(counts)
        best_gid = gid

best_minute = np.argmax(guards[best_gid])
print('part1: guard id', best_gid, 'minute', best_minute, 'result', best_gid * best_minute)


# Part 2. The guard most frequently asleep one particular minute
best_max = -1
best_gid = None
for gid, counts in guards.items():
    if max(counts) > best_max:
        best_max = max(counts)
        best_gid = gid

best_minute = np.argmax(guards[best_gid])
print('part2: guard id', best_gid, 'minute', best_minute, 'result', best_gid * best_minute)
