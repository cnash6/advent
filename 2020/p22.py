#!/usr/bin/env python

from utils import *
from collections import deque

calc_score = lambda x: sum([x*(i+1) for i,x in enumerate((x)[::-1])])

def part_one(inputs):
    p1,p2 = [[int(y) for y in x.split(':',1)[1].strip().split('\n')] for x in inputs.split('\n\n')]
    while p1 and p2:
        c1,c2 = p1.pop(0), p2.pop(0)
        res = ([c1,c2],[]) if c1>c2 else ([],[c2,c1])
        p1 += res[0]
        p2 += res[1]
    return calc_score(p1 if p1 else p2)

def endless_war(p1,p2):
    rounds = {}
    while p1 and p2:
        f1,f2 = frozenset(p1),frozenset(p2)
        if rounds.get((f1,f2), None):
            return p1,[]
        rounds[(f1,f2)] = True
        c1,c2 = p1.popleft(), p2.popleft()
        res = endless_war(deque(list(p1)[:c1]), deque(list(p2)[:c2])) if len(p1) >= c1 and len(p2) >= c2 else (([c1,c2],[]) if c1>c2 else ([],[c2,c1]))
        if res[0]:
            p1.extend([c1,c2])
        else:
            p2.extend([c2,c1])
    return p1,p2

    
def part_two(inputs):
    p1,p2 = [deque([int(y) for y in x.split(':',1)[1].strip().split('\n')]) for x in inputs.split('\n\n')]
    results = endless_war(p1,p2)
    return calc_score(list(results[0]) if results[0] else list(results[1]))


s = start_time()
# # print(part_one(open('inputs/22.1', 'r').read()))
print(part_one(open('inputs/22', 'r').read())) # 35818
end_time(s)

s = start_time()
# print(part_two(open('inputs/22.2', 'r').read()))
# print(part_two(open('inputs/22.1', 'r').read()))
print(part_two(open('inputs/22', 'r').read()))
end_time(s)
