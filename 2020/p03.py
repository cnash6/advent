#!/usr/bin/env python

from functools import reduce
from utils import *

def part_one(inputs, dx, dy):
    return sum([1 if inputs[i*dy][i*dx%len(inputs[i])] == '#' else 0 for i in range(0, len(inputs)//dy)])

def part_two(inputs, slopes):
    return reduce(lambda total, s: total * part_one(inputs, *s), slopes, 1)

inputs = togrid(aocin('inputs/03'))
inputs1 = togrid(aocin('inputs/03.1'))
slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]

# Part One 
print(part_one(inputs1, 3, 1))
print(part_one(inputs, 3, 1))

# Part Two 
print(part_two(inputs1, slopes))
print(part_two(inputs, slopes))
