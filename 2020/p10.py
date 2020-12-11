#!/usr/bin/env python

from utils import *
from functools import cache

def part_one(inputs):
    adapters = [0] + sorted([int(x) for x in inputs])
    c = [adapters[i]-adapters[i-1] for i in range(1, len(adapters))] + [3]
    return len([x for x in c if x == 1]) * len([x for x in c if x == 3])

@cache
def build_chain(curr, adapters):
    children = [build_chain(x, adapters) for x in range(curr+1, curr+4) if x in adapters]
    return sum(children) if children else 1

def part_two(inputs):
    adapters = sorted([int(x) for x in inputs])
    return build_chain(0, tuple(adapters))

ss = start_time()
# Part One 
# print(part_one(aocin('inputs/10.1')))
# print(part_one(aocin('inputs/10.2')))
print(part_one(aocin('inputs/10')))
end_time(ss)

ss = start_time()
# Part One 
# print(part_two(aocin('inputs/10.1')))
# print(part_two(aocin('inputs/10.2')))
print(part_two(aocin('inputs/10')))
end_time(ss)