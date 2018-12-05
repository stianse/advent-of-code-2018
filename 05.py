#!/usr/bin/env python3
import string

with open('05.txt') as f:
    inputs = f.read().strip()

A = inputs

def react(a):
    stack = []
    for c in a:
        if stack and c.swapcase() == stack[-1]:
            stack.pop()
        else:
            stack.append(c)
    return stack

# Part 1
print(len(react(A)))

# Part 2
best_len = len(A) + 1
for x in string.ascii_lowercase:
    a = [c for c in A if c.lower() != x]
    r = react(a)
    if len(r) < best_len:
        best_len = len(r)
print(best_len)
