#!/usr/bin/env python3
from collections import defaultdict

NUM_WORKERS = 5
MIN_TIME = 61

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



no_deps = [x for x in fwd if x not in back]
active_workers = []
total_time = 0

while True:
    no_deps.sort()
    # Can process a up to NUM_WORKERS steps in paralell
    workers_avail = NUM_WORKERS - len(active_workers)
    start_these_steps = no_deps[:workers_avail]
    for step in start_these_steps:
        no_deps.pop(0)
        time = MIN_TIME + ord(step) - ord('A')
        active_workers.append((time, step))
        print('start step', step, 'at time', total_time)

    if not active_workers:
        break

    active_workers.sort()
    done_time, done_step = active_workers.pop(0)
    active_workers = [(t-done_time, step) for t, step in active_workers]
    total_time += done_time

    # Iterate over steps that depends on the finished step and check if all
    # their deps are finished
    for s in fwd[done_step]:
        back[s].remove(done_step)
        if not back[s]:
            no_deps.append(s)

print('total time', total_time)
