#!/usr/bin/env python

from utils import *
from collections import deque
import math

def part_one(inputs, n):
    cups = deque([int(x) for x in inputs])
    current = cups[0]
    min_cup,max_cup = min(cups),max(cups)

    for _ in range(n):
        current = cups[0]
        target = current
        cups.rotate(-1)
        grab = [cups.popleft() for _ in range(3)]
        i = None
        while i == None:
            target = target - 1 if target - 1 >= min_cup else max_cup
            try:
                i = cups.index(target)
            except Exception:
                pass
        cups.rotate(-(i+1))
        cups.extendleft(grab[::-1])
        cups.rotate((i+1))

    i = cups.index(1)
    lcups = list(cups)
    return (''.join(str(x) for x in (lcups[i+1:]+lcups[:i])),cups)

def get_target(x, max_cup, exclude):
    while True:
        x = x - 1 if x-1 >= 1 else max_cup
        if x not in exclude:
            return x
    
def part_two(inputs, n, maxc=None):
    inputs = [int(x) for x in inputs]
    cups = {inputs[i]: (inputs[i+1] if i+1 < len(inputs) else (max(inputs)+1 if maxc else inputs[0])) for i in range(len(inputs))}
    min_cup,max_cup = 1,maxc if maxc else max(cups)
    if maxc:
        cups[maxc] = inputs[0]
    curr = inputs[0]
    wrapi = lambda x: x if x >= min_cup else max_cup
    getcup = lambda x: cups[x] if x in cups else x+1


    for _ in range(n):
        grab1 = getcup(curr)
        grab2 = getcup(grab1)
        grab3 = getcup(grab2)
        cups[curr] = getcup(grab3)
        target = get_target(curr, max_cup, [grab1, grab2, grab3]) 
        cups[grab3] = getcup(target)
        cups[target] = grab1
        curr = getcup(curr)

    return cups[1] * cups[cups[1]]

    

s = start_time()
# print(part_one(aocin('inputs/23.1'), 10)[0])
# print(part_one(aocin('inputs/23.1'), 100)[0])
print(part_one(aocin('inputs/23'), 100)[0])
end_time(s)

s = start_time()
# print(part_two(aocin('inputs/23.1'), 10000000, 1000000))
print(part_two(aocin('inputs/23'), 10000000, 1000000))
end_time(s)
