#!/usr/bin/env python
from functools import reduce

from utils import aocin

def part_one(inputs: list[str]):

    limits = {
        "red": 12, 
        "green": 13,
        "blue": 14
    }

    total = 0
    for game in inputs: 
        game_id, cubes = game.split(": ")
        game_id = int(game_id.split(" ")[1])

        failed = False
        for cube in [x for y in [j.split(", ") for j in cubes.split("; ")] for x in y]:
            n, c = cube.split(" ")
            if int(n) > limits[c]:
                failed = True
        if not failed:
            total += game_id

    return total
        

def part_two(inputs: list[str]):
    total = 0
    for game in inputs: 
        _, cubes = game.split(": ")

        max_cubes = {"red": 0, "green": 0,"blue": 0}

        for cube in [x for y in [j.split(", ") for j in cubes.split("; ")] for x in y]:
            n, color = cube.split(" ")
            max_cubes[color] = max(max_cubes[color], int(n))
        total += reduce(lambda x, y: x*y, max_cubes.values())

    return total


print(part_one(aocin("inputs/02.1")))
print(part_one(aocin("inputs/02")))

print(part_two(aocin("inputs/02.1")))
print(part_two(aocin("inputs/02")))



