#!/usr/bin/env python

from itertools import combinations
from functools import reduce

def expenses(input_file, n):
    f = open(input_file, 'r')
    expenses = [int(x) for x in f]

    for combination in combinations(expenses, n):
        if sum(combination) == 2020:
            return reduce(lambda x, y: x * y, list(combination))

# Part One
print(expenses('inputs/01.1', 2)) # 514579
print(expenses('inputs/01', 2))

# part Two
print(expenses('inputs/01.1', 3)) # 241861950
print(expenses('inputs/01', 3)) 