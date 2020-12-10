#!/usr/bin/env python

from utils import *
from collections import defaultdict

def part_one(inputs):
    MAX_DIFF = 3
    adapters = sorted([int(x) for x in inputs])
    diffs = defaultdict(int)

    prev = 0
    for adapter in adapters:
        diffs[adapter-prev]+=1
        prev = adapter
    diffs[3]+=1

    return diffs[1] * diffs[3]

def build_chain(curr, memo, adapters):
    if curr in memo:
        return memo[curr], memo
    if not any([x in adapters for x in range(curr+1, curr+4)]):
        return 1, memo
    
    myval = 0
    for i,x in enumerate(range(curr+1, curr+4)):
        if x in adapters:
            childres = build_chain(x, memo, [y for y in adapters if y > x])
            myval+= childres[0]
            memo = childres[1]
    memo[curr] = myval
    return myval, memo

def part_two(inputs):
    adapters = sorted([int(x) for x in inputs])
    return build_chain(0, {}, adapters)[0]

ss = start_time()
# Part One 
print(part_one(aocin('inputs/10.1')))
print(part_one(aocin('inputs/10.2')))
print(part_one(aocin('inputs/10')))
end_time(ss)

ss = start_time()
# Part One 
print(part_two(aocin('inputs/10.1')))
print(part_two(aocin('inputs/10.2')))
print(part_two(aocin('inputs/10')))
end_time(ss)