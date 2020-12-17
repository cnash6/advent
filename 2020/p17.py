#!/usr/bin/env python

from utils import *
from itertools import product


# def print_cubes(cubes):
#     minx,maxx = min(cubes.items(), key=lambda item: item[0][0])[0][0], max(cubes.items(), key=lambda item: item[0][0])[0][0]
#     miny,maxy = min(cubes.items(), key=lambda item: item[0][1])[0][1], max(cubes.items(), key=lambda item: item[0][1])[0][1]
#     minz,maxz = min(cubes.items(), key=lambda item: item[0][2])[0][2], max(cubes.items(), key=lambda item: item[0][2])[0][2]

#     print(cubes)
#     for k in range(min(minz,0), maxz+1):
#         print(f'z={k}')
#         for j in range(min(miny,0), maxy+1):
#             print(''.join([cubes.get((i,j,k), '.') for i in range(min(minx,0), maxx+1)]))
#         print()

def minmax(d, cubes):
    return min(cubes.items(), key=lambda item: item[0][d])[0][d], max(cubes.items(), key=lambda item: item[0][d])[0][d]
    
def neigbors_3d(cube, cubes):
    return len([1 for i in range(cube[0]-1, cube[0]+2) for j in range(cube[1]-1, cube[1]+2) for k in range(cube[2]-1, cube[2]+2) if cubes.get((i,j,k)) == '#' and (i,j,k) != cube])

def num_active_neigbors(cube, cubes):
    return len([x for x in product(*[list(range(cube[d]-1, cube[d]+2)) for d in range(len(cube))]) if cubes.get(x) == '#' and x != cube])

def part_one(inputs, n):
    cubes = {(i,j,0): x for j,y in enumerate(inputs) for i,x in enumerate(y) if x == '#'}
    for _ in range(n):
        newcubes = {}

        minx,maxx = minmax(0, cubes)
        miny,maxy = minmax(1, cubes)
        minz,maxz = minmax(2, cubes)
        for i,j,k in [(i,j,k) for i in range(minx-1, maxx+2) for j in range(miny-1, maxy+2) for k in range(minz-1, maxz+2)]:
            val = cubes.get((i,j,k))
            nactiven = num_active_neigbors((i,j,k), cubes)
            if (val and 2<=nactiven<=3) or (not val and nactiven==3):
                newcubes[(i,j,k)] = '#'
        cubes = newcubes

    return len(cubes)

# def part_one(inputs, n):
#     cubes = {(i,j,0, 0): x for j,y in enumerate(inputs) for i,x in enumerate(y) if x == '#'}
#     for _ in range(n):
#         newcubes = {}
#         minmax = lambda d: 

#         minx,maxx = minmax(0)
#         miny,maxy = min(cubes.items(), key=lambda item: item[0][1])[0][1], max(cubes.items(), key=lambda item: item[0][1])[0][1]
#         minz,maxz = min(cubes.items(), key=lambda item: item[0][2])[0][2], max(cubes.items(), key=lambda item: item[0][2])[0][2]
#         for i,j,k in [(i,j,k) for i in range(minx-1, maxx+2) for j in range(miny-1, maxy+2) for k in range(minz-1, maxz+2)]:
#             val = cubes.get((i,j,k))
#             nactiven = num_active_neigbors((i,j,k), cubes)
#             if (val and 2<=nactiven<=3) or (not val and nactiven==3):
#                 newcubes[(i,j,k)] = '#'
#         cubes = newcubes

#     return len(cubes)

s = start_time()
print(part_one(aocin('inputs/17.1'), 6)) 
print(part_one(aocin('inputs/17'), 6)) 
end_time(s)

# s = start_time()
# print(part_two(aocin('inputs/17.1'), 6)) 
# # print(part_two(aocin('inputs/17'), 6)) 
# end_time(s)
