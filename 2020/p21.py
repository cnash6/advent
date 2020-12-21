#!/usr/bin/env python

from utils import *
from collections import defaultdict

def part_one(inputs):
    mappings = {}
    full_ingredients = []
    for line in inputs:
        ingredients, alergens = line[:-1].split(' (contains ')
        ingredients = ingredients.split(' ')
        full_ingredients += ingredients
        alergens = alergens.split(', ')
        for alergen in alergens:
            mappings[alergen] = mappings[alergen].intersection(set(ingredients)) if alergen in mappings else set(ingredients)

    bad = []
    while mappings:
        small = sorted(mappings.items(), key=lambda x: len(x[1]))[0]
        bad.append((small[1].pop(), small[0]))
        del mappings[small[0]]
        for key in mappings.keys():
            if bad[-1][0] in mappings[key]: mappings[key].remove(bad[-1][0])

    return sum(1 for x in full_ingredients if x not in [x[0] for x in bad]),bad

def part_two(inputs):
    bad = part_one(inputs)[1]
    return ','.join([x for x,y in sorted(bad, key=lambda x: x[1])])

s = start_time()
print(part_one(aocin('inputs/21.1'))[0])
print(part_one(aocin('inputs/21'))[0])
end_time(s)

s = start_time()
print(part_two(aocin('inputs/21.1')))
print(part_two(aocin('inputs/21')))
end_time(s)
