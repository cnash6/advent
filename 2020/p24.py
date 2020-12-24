#!/usr/bin/env python

from utils import *
from itertools import product

moves = {
    'e': (2,0),
    'w': (-2,0),
    'ne': (1,1),
    'nw': (-1,1),
    'se': (1,-1),
    'sw': (-1,-1)
}

def getmove(instruction):
    i = 1 if instruction[0] in ['e', 'w'] else 2
    return moves[instruction[:i]], instruction[i:]

def do_it(inputs, fliprule):
    tiles = {}
    for instruction in inputs:
        tile = (0,0)
        while instruction:
            move, instruction = getmove(instruction)
            tile = (tile[0]+move[0],tile[1]+move[1])
        tiles[tile] = fliprule(tile,tiles)
    return tiles
    
fliprule = lambda tile,tiles: not tiles[tile] if tile in tiles else True

def part_one(inputs):
    tiles = do_it(inputs, fliprule)
    return len([x for x in tiles.values() if x])

def p2rule(tile, tiles):
    adj = sum([1 for y in [tiles[(tile[0]+x[0],tile[1]+x[1])] for x in moves.values() if (tile[0]+x[0],tile[1]+x[1]) in tiles] if y])
    return (tiles.get(tile, False) and adj in [1,2]) or (not tiles.get(tile, False) and adj == 2)

def part_two(inputs, n):
    tiles = do_it(inputs, fliprule)
    for _ in range(n):
        minx,maxx = min(tiles.keys(), key=lambda x: x[0])[0], max(tiles.keys(), key=lambda x: x[0])[0] 
        miny,maxy = min(tiles.keys(), key=lambda x: x[1])[1], max(tiles.keys(), key=lambda x: x[1])[1] 
        tiles = {y: p2rule(y,tiles) for y in [x for x in product(range(minx-2,maxx+2),range(miny-2,maxy+2))]}
    return len([x for x in tiles.values() if x])


s = start_time()
# print(part_one(aocin('inputs/24.1')))
print(part_one(aocin('inputs/24')))
end_time(s)

s = start_time()
# print(part_two(aocin('inputs/24.1'), 100))
print(part_two(aocin('inputs/24'), 100))
end_time(s)
