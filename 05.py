#!/usr/bin/env python3

with open('05.txt') as f:
    inputs = f.read().replace('\n', '')

A = [ord(c) for c in inputs]
D = ord('a') - ord('A')

def react(a):
    i = 0
    while i < len(a) - 1:
        if abs(a[i] - a[i+1]) == D:
            a = a[:i] + a[i+2:]
            if i > 0:
                i -= 1
        else:
            i += 1
    return a

# Part 1
print(len(react(A)))

# Part 2
best_len = None
for x in range(ord('A'), ord('Z') + 1):
    a = [c for c in A if c not in (x, x + D)]
    r = react(a)
    if best_len is None or len(r) < best_len:
        best_len = len(r)
print(best_len)
