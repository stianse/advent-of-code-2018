#!/usr/bin/env python3
import re
import numpy as np

with open('16.txt') as f:
    INPUT, PROGRAM = f.read().split('\n\n\n')

def parse_all_ints(s):
    return [int(x) for x in re.findall('-?\d+', s)]

def addr(regs, a, b):
    return regs[a] + regs[b]

def addi(regs, a, b):
    return regs[a] + b

def mulr(regs, a, b):
    return regs[a] * regs[b]

def muli(regs, a, b):
    return regs[a] * b

def banr(regs, a, b):
    return regs[a] & regs[b]

def bani(regs, a, b):
    return regs[a] & b

def borr(regs, a, b):
    return regs[a] | regs[b]

def bori(regs, a, b):
    return regs[a] | b

def setr(regs, a, b):
    return regs[a]

def seti(regs, a, b):
    return a

def gtir(regs, a, b):
    return 1 if a > regs[b] else 0

def gtri(regs, a, b):
    return 1 if regs[a] > b else 0

def gtrr(regs, a, b):
    return 1 if regs[a] > regs[b] else 0

def eqir(regs, a, b):
    return 1 if a == regs[b] else 0

def eqri(regs, a, b):
    return 1 if regs[a] == b else 0

def eqrr(regs, a, b):
    return 1 if regs[a] == regs[b] else 0

OPS = [addr, addi, mulr, muli, banr, bani, borr, bori,
       setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]

count = 0
possible = np.ones((16,16), dtype=int)
for data in INPUT.split('\n\n'):
    regs_before, instruction, regs_after = data.splitlines()
    regs_before = parse_all_ints(regs_before)
    opc, a, b, c = parse_all_ints(instruction)
    regs_after = parse_all_ints(regs_after)

    match = 0
    for opid, op in enumerate(OPS):
        if op(regs_before, a, b) == regs_after[c]:
            match += 1
        else:
            possible[opid, opc] = 0
    if match >= 3:
        count += 1

print('Part1', count)

# Map opcodes with functions
opsmap = [None] * 16
for i in range(16):
    # Find an opcode that only has one possible operation
    opid = np.argwhere(np.sum(possible, axis=1) == 1)[0][0]
    opc = np.argwhere(possible[opid] == 1)[0][0]
    opsmap[opc] = OPS[opid]
    possible[:,opc] = 0

regs = [0] * 4
for line in PROGRAM.splitlines():
    if not line:
        continue
    opc, a, b, c = parse_all_ints(line)
    regs[c] = opsmap[opc](regs, a, b)

print('Part2', regs[0])
