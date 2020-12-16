#!/usr/bin/env python

from utils import *
import math
from collections import defaultdict

def part_one(inputs):
    chunks = open(inputs, 'r').read().split('\n\n', 1)
    rules = [tuple(y.split('-')) for y in (','.join([','.join(x.split(': ')[1].split(' or ')) for x in chunks[0].split('\n')])).split(',')]
    tickets = [[int(y) for y in x.split(',')] for x in chunks[1].split('\n') if x and x[-1] != ':']
    errors = []
    badtix = []
    for ticket in tickets:
        err = [x for x in ticket if not any([int(y[0]) <= x <= int(y[1]) for y in rules])]
        errors = errors + err
        badtix = badtix + ([tuple(ticket)] if err else [])
    return sum(errors), badtix
    
def part_two(inputs):
    chunks = open(inputs, 'r').read().split('\n\n', 1)
    rules = {y[0]: [tuple(z.split('-')) for z in y[1].split(' or ')] for y in [x.split(': ') for x in chunks[0].split('\n')]}
    to_exclude = part_one(inputs)[1]
    tickets = [ticket for ticket in [[int(y) for y in x.split(',')] for x in chunks[1].split('\n') if x and x[-1] != ':'] if tuple(ticket) not in to_exclude]
    rulemap = defaultdict(list)
    for rule, defn in rules.items():
        for i in range(len(tickets[0])):
            if all([any([int(r[0]) <= ticket[i] <= int(r[1]) for r in defn]) for ticket in tickets[1:]]):
                rulemap[rule].append(i)
    # we have a rule map with all possibilities
    final = []
    while rulemap: # I hate this
        found = sorted(rulemap.items(), key=lambda x: len(x[1]))[0]
        found = (found[0], found[1][0])
        for r in rulemap:
            l = rulemap[r]
            l.remove(found[1])
            rulemap[r] = l
        del rulemap[found[0]]
        final.append(found)
    
    return math.prod([tickets[0][x[1]] for x in final if 'departure' in x[0]])


s = start_time()
print(part_one('inputs/16.1')[0]) 
print(part_one('inputs/16')[0])
end_time(s)

s = start_time()
print(part_two('inputs/16.2')) 
print(part_two('inputs/16'))
end_time(s)
