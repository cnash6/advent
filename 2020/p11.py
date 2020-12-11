#!/usr/bin/env python

from utils import *
from itertools import product
from copy import deepcopy

def tick_seats(seats, nieghborfn, numneighbors):
    newseats = deepcopy(seats)
    changed = False
    for j in range(len(seats)):
        for i,seat in enumerate(seats[j]):   
            occupied_neighbors = nieghborfn(i, j, seats)
            if seat == 'L' and not occupied_neighbors:
                newseats[j][i] = '#'
                changed = True
            elif seat == '#' and len(occupied_neighbors) >= numneighbors:
                newseats[j][i] = 'L'
                changed = True
    return changed, newseats

def intersect_seat(x, y, dx, dy, seats):
    poss = seats[y+dy][x+dx] if x+dx >= 0 and x+dx < len(seats[0]) and y+dy >= 0 and y+dy < len(seats) else 'None'
    return poss if poss != '.' or poss == 'None' else intersect_seat(x+dx, y+dy, dx, dy, seats)
    
def part_one(inputs):
    seats = [[y for y in x] for x in inputs]
    nieghborfn = lambda i, j, s: [s[x[1]][x[0]] for x in product(range(i-1, i+2),  range(j-1, j+2)) if x[1] >= 0 and x[1] < len(s) and x[0] >= 0 and x[0] < len(s[0]) and (x[1],x[0]) != (j,i) and s[x[1]][x[0]] == '#']
    while True:        
        changed, seats = tick_seats(seats, nieghborfn, 4)
        if not changed:
            return len([y for y in ''.join([''.join(x) for x in seats]) if y == '#'])

def part_two(inputs):
    seats = [[y for y in x] for x in inputs]
    nieghborfn = lambda i, j, s: [y for y in [intersect_seat(i, j, x[0], x[1], seats) for x in [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]] if y == '#']
    while True:        
        changed, seats = tick_seats(seats, nieghborfn, 5)
        if not changed:
            return len([y for y in ''.join([''.join(x) for x in seats]) if y == '#'])



s = start_time()
# Part One 
print(part_one(aocin('inputs/11.1')))
print(part_one(aocin('inputs/11')))
end_time(s)

s = start_time()
# Part One 
print(part_two(aocin('inputs/11.1')))
print(part_two(aocin('inputs/11')))
end_time(s)