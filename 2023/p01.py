#!/usr/bin/env python
import re

def part_one(fname):
    with open(fname, 'r') as f:
        lines = f.readlines()

    vals = []
    for line in lines:
        nums = [x for x in line if x.isnumeric()]
        vals.append(int(nums[0]+nums[-1]))
    return sum(vals)

replace = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

def find_numeric(astr: str, r: bool = False) -> str:
    for i,c in enumerate(astr):
        if c.isnumeric():
            return c
        for s,d in replace.items():
            if astr[i:].find(s if not r else s[::-1] ) == 0:
                return d
        

def part_two(fname):
    with open(fname, 'r') as f:
        lines = f.readlines()

    vals = []
    for line in lines:

        first = find_numeric(line)
        last = find_numeric(line[::-1], r=True)
        
        vals.append(int(first+last))
            

        # vals.append(int(nums[0]+nums[-1]))
    return sum(vals)

    
print(part_one('inputs/01.1'))
print(part_one('inputs/01'))

print(part_two('inputs/01.2'))
print(part_two('inputs/01'))


