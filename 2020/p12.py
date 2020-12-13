#!/usr/bin/env python

from utils import *
from math import *

def part_one(inputs):
    instructions = [(x[0], int(x[1:])) for x in inputs]
    ship = (0,0,90)
    compass = {0: 'N',90:'E',180:'S',270:'W'}
    move = {
        'N': lambda ship, n: (ship[0], ship[1]+n, ship[2]),
        'S': lambda ship, n: (ship[0], ship[1]-n, ship[2]),
        'E': lambda ship, n: (ship[0]+n, ship[1], ship[2]),
        'W': lambda ship, n: (ship[0]-n, ship[1], ship[2])
    }

    for instruction, n in instructions:
        if instruction in ['N','S','E','W']:
            ship = move[instruction](ship, n)
        elif instruction in ['L','R']:
            ship = ship[:2] + ((ship[2] + n) % 360,) if instruction == 'R' else ship[:2] + (abs((ship[2] - n) % 360),)
        else:
            ship = move[compass[ship[2]]](ship, n)

    return manhattan((ship[0], ship[1]), (0,0))


def part_two(inputs):
    instructions = [(x[0], int(x[1:])) for x in inputs]
    ship = (0,0)
    waypoint = (10,1)
    move = {
        'N': lambda p, n: (p[0], p[1]+n),
        'S': lambda p, n: (p[0], p[1]-n),
        'E': lambda p, n: (p[0]+n, p[1]),
        'W': lambda p, n: (p[0]-n, p[1])
    }

    for instruction, n in instructions:
        if instruction in ['N','S','E','W']:
            waypoint = move[instruction](waypoint, n)
        elif instruction in ['L','R']:
            rads = radians(n) if instruction == 'L' else radians(-1*n)
            waypoint = (round(waypoint[0]*cos(rads)-waypoint[1]*sin(rads)), round(waypoint[1]*cos(rads)+waypoint[0]*sin(rads)))
        else:
            ship = (ship[0]+waypoint[0]*n, ship[1]+waypoint[1]*n)
    return manhattan((ship[0], ship[1]), (0,0))

s = start_time()
# Part One 
print(part_one(aocin('inputs/12.1')))
print(part_one(aocin('inputs/12')))
end_time(s)

s = start_time()
# Part One 
print(part_two(aocin('inputs/12.1')))
print(part_two(aocin('inputs/12')))
end_time(s)