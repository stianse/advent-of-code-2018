#!/usr/bin/env python3

INPUT = '633601'
A = [int(x) for x in INPUT]
ALEN = len(A)

scores = [3, 7]
elf1, elf2 = 0, 1

ans = None
while ans is None:
    total = scores[elf1] + scores[elf2]
    scores += divmod(total, 10) if total >= 10 else [total]
    elf1 = (elf1 + scores[elf1] + 1) % len(scores)
    elf2 = (elf2 + scores[elf2] + 1) % len(scores)
    if scores[-ALEN:] == A:
        ans = len(scores) - ALEN
    if total >= 10 and scores[-ALEN-1:-1] == A:
        ans = len(scores) - ALEN - 1

print('Part 1', ''.join(map(str, scores[int(INPUT):int(INPUT)+10])))
print('Part 2', ans)
