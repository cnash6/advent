#!/usr/bin/env python

from utils import *

def part_one(fname):
    with open(fname, 'r') as f:
        elves = f.read().split('\n\n')
        return max(sum([int(y) for y in x.split('\n')]) for x in elves)


def part_two(fname):
    with open(fname, 'r') as f:
        elves = f.read().split('\n\n')
        return sum(sorted([sum([int(y) for y in x.split('\n')]) for x in elves], reverse=True)[:3])
        

    
print(part_one('inputs/01.1'))
print(part_one('inputs/01'))

print(part_two('inputs/01.1'))
print(part_two('inputs/01'))
