#!/usr/bin/env python

from utils import *

elf_plays = {'A': 1, 'B': 2, 'C': 3}
my_plays = {'X': 1, 'Y': 2, 'Z': 3}
 
def game_points(elf, me):

    if elf_plays[elf] == my_plays[me]:
        return 3
    if my_plays[me] - elf_plays[elf] in (1,-2):
        return 6
    return 0

def part_one(inputs):
    games = [x.split(' ') for x in inputs]

    return sum(my_plays[x[1]] + game_points(*x) for x in games)


def part_two(inputs):
    games = [x.split(' ') for x in inputs]

    elf_play_keys = list(elf_plays.keys())

    result = 0
    for game in games:
        if game[1] == 'X': # lose
            result += 0 + elf_plays[elf_play_keys[(elf_play_keys.index(game[0])-1)%3]]
        if game[1] == 'Y': # tie
            result += 3 + elf_plays[elf_play_keys[elf_play_keys.index(game[0])]]
        if game[1] == 'Z': # win
            result += 6 + elf_plays[elf_play_keys[(elf_play_keys.index(game[0])+1)%3]]

    return result
    

print(part_one(aocin("inputs/02.1")))
print(part_one(aocin("inputs/02")))

print(part_two(aocin("inputs/02.1")))
print(part_two(aocin("inputs/02")))

