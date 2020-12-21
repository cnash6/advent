#!/usr/bin/env python

from utils import *

edgefns = {
    'top_edge': lambda t: t[1],
    'bottom_edge': lambda t: t[-1],
    'left_edge': lambda t: [y[0] for y in t],
    'right_edge': lambda t: [y[-1] for y in t]
}


def fit_tiles(tile1, tile2):
    for fk,fn in edgefns.items():
        tile1edge = fn(tile1)
        for fk2,fn2 in edgefns.items():
            tile2edge = fn2(tile2)
            if tuple(tile1edge) == tuple(tile2edge):
                return fk,fk2

def part_one(inputs):
    tiles = {x[0][5:-1]:[[i for i in j] for j in x[1].split('\n')]  for x in [y.split('\n',1) for y in inputs.split('\n\n')]}
    unmatched = [tile for tile in tiles]
    # while unmatched:
    tile = unmatched[0] # 2311
    for test in [x for x in tiles if x != tile]:
        fit = fit_tiles(tiles[tile], tiles[test])
        if fit:
            print(f'tile {tile} {fit[0]} fits tile {test} {fit[1]}')

    # return tiles


s = start_time()
print(part_one(open('inputs/20.1', 'r').read())) 
# print(part_one(open('inputs/20', 'r').read())) 
end_time(s)
