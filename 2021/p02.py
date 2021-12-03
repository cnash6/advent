#!/usr/bin/env python

from utils import *


def part_one(inputs):
    steps = [x.split(" ") for x in inputs]
    x, y = 0, 0
    moves = {
        "up": lambda x, y, delta: (x, y - int(delta)),
        "down": lambda x, y, delta: (x, y + int(delta)),
        "forward": lambda x, y, delta: (x + int(delta), y),
    }

    for step in steps:
        x, y = moves[step[0]](x, y, step[1])
    return x * y


def part_two(inputs):
    steps = [x.split(" ") for x in inputs]
    x,y,aim = 0,0,0

    for step in steps:
        x,y,aim = {
            "up": lambda x, y, aim, delta: (x, y, aim - int(delta)),
            "down": lambda x, y, aim, delta: (x, y, aim + int(delta)),
            "forward": lambda x, y, aim, delta: (
                x + int(delta),
                y + aim * int(delta),
                aim,
            ),
        }[step[0]](x, y, aim, step[1])
    return x * y


print(part_one(aocin("inputs/02.1")))
print(part_one(aocin("inputs/02")))

print(part_two(aocin("inputs/02.1")))
print(part_two(aocin("inputs/02")))
