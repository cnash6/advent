#!/usr/bin/env python
# coding: utf-8

from collections import defaultdict
from math import ceil

def get_needed_ore(desired, product):
    recipe = reactions.get(product)
    extra = extras[product]
    recipe_multiples = ceil(max([desired - extra, 0]) / recipe[0])
    if product != 'ORE':
        extras[product] = (recipe[0] * recipe_multiples) - (desired - extra)
    needed = 0
    for ingredient in recipe[1]:
        if ingredient[1] == 'ORE':
            needed += recipe_multiples * ingredient[0]
        else:
            needed += get_needed_ore(ingredient[0] * recipe_multiples, ingredient[1])
    return needed

# Main      
f = open('assets/14.txt', 'r')
reactions = {z[0][1]: (int(z[0][0]),[(int(zz[0]), zz[1]) for zz in [xx.split() for xx in z[1]]]) for z in [(tuple(y[1].split(' ')), y[0].split(', ')) for y in [x.rstrip().split(' => ') for x in f]]}


# for r in reactions:
#     print(f'{r}: {reactions[r]}')

# Part 1
extras = defaultdict(int)
needed = get_needed_ore(1,'FUEL')
print(needed)

# Part 2
ORE = 1000000000000
i = 1
last = i
while True:
    extras = defaultdict(int)
    needed = get_needed_ore(last+i, 'FUEL')
    if needed == ORE:
        print(f'{last+i}')
        break
    elif needed > ORE:
        if i == 1:
            print(f'{last+i-1}')
            break
        i = 1
    else:
        last = last+i
        i = i * 2
        
        

