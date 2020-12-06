#!/usr/bin/env python

from utils import *
import re

def partone(inputs): 
    to_bin = lambda seatstring, oneval: int(''.join(['1' if c is oneval else '0' for c in seatstring]), 2)
    ids = [(to_bin(x[:7], 'B') * 8) + to_bin(x[-3:], 'R') for x in inputs]
    return ids

inputs = aocin('inputs/05')
inputs1 = aocin('inputs/05.1')

# Part One 
print(max(partone(inputs1)))
print(max(partone(inputs)))

# Part Two
ids = sorted(partone(inputs))
for i in range(1, len(ids)):
    if ids[i] != ids[i-1]+1:
        print(ids[i]-1)
