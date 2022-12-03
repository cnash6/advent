#!/usr/bin/env python

from utils import *

def priority(c):
    return ord(c)-38 if ord(c) < 91 else ord(c)-96

def part_one(inputs):
    return sum(priority(list(set(x[:(len(x)//2)]) & set(x[(len(x)//2):]))[0]) for x in inputs)

def part_two(inputs):
    return sum(priority(list(set(inputs[i*3]) & set(inputs[(i*3)+1]) & set(inputs[(i*3)+2]))[0]) for i in range(len(inputs)//3))



print(part_one(aocin("inputs/03.1")))
print(part_one(aocin("inputs/03")))

print(part_two(aocin("inputs/03.1")))
print(part_two(aocin("inputs/03")))

