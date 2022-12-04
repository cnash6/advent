#!/usr/bin/env python

from utils import aocin

def do_it(inputs):
    result1, result2 = 0, 0
    for pair in inputs:
        # build sets for camp ranges
        a,b = (set(range(*(z if i == 0 else z+1 for i,z in enumerate(int(y) for y in x.split('-'))))) for x in pair.split(','))
        result1 += 1 if a <= b or b <= a else 0
        result2 += 1 if a & b else 0
    return result1, result2

print(do_it(aocin("inputs/04.1")))
print(do_it(aocin("inputs/04")))

