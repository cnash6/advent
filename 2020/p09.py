#!/usr/bin/env python

from utils import *
from itertools import combinations

def part_one(inputs, n):
    nums = [int(x) for x in inputs]
    for i in range(n, len(nums)):
        if not any([sum(c) == nums[i] for c in combinations(nums[i-n: i], 2)]):
            return nums[i]

def part_two(inputs, n):
    target = part_one(inputs, n)
    nums = [int(x) for x in inputs]

    for i in range(len(nums)):
        acc = 0
        for j in range(i, len(nums)):
            acc+= nums[j]
            if acc == target:
                tmp = nums[i:j+1]
                return sum([min(tmp), max(tmp)])
            if acc > target:
                break

s = start_time()
# Part One 
# print(part_one(aocin('inputs/09.1'), 5))
print(part_one(aocin('inputs/09'), 25))

# # Part Two 
# print(part_two(aocin('inputs/09.1'), 5))
print(part_two(aocin('inputs/09'), 25))
end_time(s)