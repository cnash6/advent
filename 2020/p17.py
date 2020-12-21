#!/usr/bin/env python

from utils import *
from itertools import product

def minmax(d, cubes):
    return (min(cubes.items(), key=lambda item: item[0][d])[0][d]-1, max(cubes.items(), key=lambda item: item[0][d])[0][d]+2)

def num_active_neigbors(cube, cubes):
    return len([x for x in product(*[list(range(cube[d]-1, cube[d]+2)) for d in range(len(cube))]) if cubes.get(x) == '#' and x != cube])

def doit(inputs, iterations, dimensions):
    cubes = {(i,j)+tuple([0 for z in range(dimensions-2)]): x for j,y in enumerate(inputs) for i,x in enumerate(y) if x == '#'}
    for _ in range(iterations):
        newcubes = {}
        for cube in product(*[list(range(*minmax(d, cubes))) for d in range(dimensions)]):
            val = cubes.get(cube)
            nactiven = num_active_neigbors(cube, cubes)
            if (val and 2<=nactiven<=3) or (not val and nactiven==3):
                newcubes[cube] = '#'
        cubes = newcubes
    return len(cubes)

s = start_time()
# print(doit(aocin('inputs/17.1'), 6, 3)) 
print(doit(aocin('inputs/17'), 6, 3)) 
end_time(s)

s = start_time()
# print(doit(aocin('inputs/17.1'), 6, 4)) 
print(doit(aocin('inputs/17'), 6, 4)) 
# print(doit(aocin('inputs/17'), 6, 5)) 
end_time(s)

s = start_time() 
print(doit(aocin('inputs/17'), 6, 5)) 
end_time(s)