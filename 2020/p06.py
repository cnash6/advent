#!/usr/bin/env python

from collections import Counter

def part_one(inputs): 
    return sum([len(set(x.replace('\n',''))) for x in inputs.split('\n\n')])

def part_two(inputs): 
    return sum([sum([1 if c[1] == len(group) else 0 for c in Counter("".join(group).replace('\n', '')).items()]) for group in [x.split('\n') for x in inputs.split('\n\n')]])


# Part One 
print(part_one(open('inputs/06.1', 'r').read()))
print(part_one(open('inputs/06', 'r').read()))

# Part Two 
print(part_two(open('inputs/06.1', 'r').read()))
print(part_two(open('inputs/06', 'r').read()))
