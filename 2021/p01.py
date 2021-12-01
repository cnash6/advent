#!/usr/bin/env python

from utils import *

def part_one(inputs):
    return sum(1 if int(inputs[i+1]) > int(inputs[i]) else 0 for i in range(len(inputs)-1))

def part_two(inputs):
    return sum(1 if sum(int(x) for x in inputs[i+1:i+4]) > sum(int(x) for x in inputs[i:i+3]) else 0 for i in range(len(inputs)-3))
    
# print(part_one(aocin('inputs/01.1')))
print(part_one(aocin('inputs/01')))

# print(part_two(aocin('inputs/01.1')))
print(part_two(aocin('inputs/01')))

