#!/usr/bin/env python
# coding: utf-8

from math import ceil

# Main      
f = open('assets/16.txt', 'r')
signal_in = [int(x) for x in f.read().rstrip()]

# Part 1

def get_pattern(i, length):
    return ([x for x in PATTERN for _ in range(i)] * max(length // (len(PATTERN)*i)+1,1))[1:length+1]

signal = signal_in[:]
PATTERN = [0, 1, 0, -1]
N = 100

# Horribly inneficient naive solution:
for _ in range(N):
    signal = [abs(sum([x[0]*x[1] for x in zip(signal, get_pattern(y+1, len(signal)))]))%10 for y in range(len(signal))]
print("".join([str(x) for x in signal])[:8])

# Part 2

from itertools import accumulate

#  ...part 1 strategy not gonna work.. one pass takes > 15 mins
signal = signal_in[:] * 10000
offset = int("".join([str(x) for x in signal])[:7])

# Observation: Once we get past n/2 items in the sequence, the pattern mulipliers will always be ...0,0,0,1,1,1... 
# offset is greater than n/2, so multipliers don't matter, can just sum the elements without worrying about multiplying
# last item is always the same, so start from the back and sum up to offset 

signal = signal[offset:][::-1] # reversed (list of values at index > offset)
for _ in range(N):
    signal = [x % 10 for x in accumulate(signal)]
print("".join(str(x) for x in signal[:-9:-1]))
    