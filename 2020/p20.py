#!/usr/bin/env python

from utils import *

edgefns = {
    'top_edge': lambda t: t[0],
    'bottom_edge': lambda t: t[-1],
    'left_edge': lambda t: [y[0] for y in t],
    'right_edge': lambda t: [y[-1] for y in t]
}
rotate_clockwise = lambda x: [list(y) for y in list(zip(*x[::-1]))]
flipx = lambda y: [x[::-1] for x in y]
flipy = lambda t: t[::-1]

def minmax(tiles,i): 
    return min(tiles.values(), key=lambda x: x['coords'][i])['coords'][i], max(tiles.values(), key=lambda x: x['coords'][i])['coords'][i] 

def fit_tiles(tile1, tile2):
    # top
    tile1edge = edgefns['top_edge'](tile1)
    for i in range(4):
        tile2 = rotate_clockwise(tile2)
        try:
            if tuple(tile1edge) == tuple(edgefns['bottom_edge'](tile2)):
                return tile2,(0,-1)
        except:
            print(tile2)
            raise 'crap'
        if tuple(tile1edge) == tuple(edgefns['bottom_edge'](flipx(tile2))):
            return flipx(tile2),(0,-1)
    # right
    tile1edge = edgefns['right_edge'](tile1)
    for i in range(4):
        tile2 = rotate_clockwise(tile2)
        if tuple(tile1edge) == tuple(edgefns['left_edge'](tile2)):
            return tile2,(1,0)
        if tuple(tile1edge) == tuple(edgefns['left_edge'](flipy(tile2))):
            return flipy(tile2),(1,0)
    # bottom
    tile1edge = edgefns['bottom_edge'](tile1)
    for i in range(4):
        tile2 = rotate_clockwise(tile2)
        if tuple(tile1edge) == tuple(edgefns['top_edge'](tile2)):
            return tile2,(0,1)
        if tuple(tile1edge) == tuple(edgefns['top_edge'](flipx(tile2))):
            return flipx(tile2),(0,1)
    # left
    tile1edge = edgefns['left_edge'](tile1)
    for i in range(4):
        tile2 = rotate_clockwise(tile2)
        if tuple(tile1edge) == tuple(edgefns['right_edge'](tile2)):
            return tile2,(-1,0)
        if tuple(tile1edge) == tuple(edgefns['right_edge'](flipy(tile2))):
            return flipy(tile2),(-1,0)
    return None,None

def part_one(inputs):
    tiles = {x[0][5:-1]:{'tile': [[i for i in j] for j in x[1].split('\n')], 'fits': []}  for x in [y.split('\n',1) for y in inputs.split('\n\n')]}
    unplaced = [tile for tile in tiles]
    starting_tile_id = unplaced[0]
    del unplaced[0]
    tiles[starting_tile_id]['tile'] = tiles[starting_tile_id]['tile'][::-1]
    tiles[starting_tile_id]['coords'] = (0,0)
    i=0
    while unplaced and i < 1000*len(unplaced):
        to_place = unplaced[i%len(unplaced)]
        for placed in [x for x in tiles if 'coords' in tiles[x]]:
            ptile,dxy = fit_tiles(tiles[placed]['tile'], tiles[to_place]['tile'])
            if ptile:
                tiles[to_place]['tile'] = ptile
                tiles[to_place]['coords'] = (tiles[placed]['coords'][0] + dxy[0], tiles[placed]['coords'][1] + dxy[1])
                del unplaced[i%len(unplaced)]
                i-=1
                break
        i+=1

    minx,maxx = minmax(tiles, 0)
    miny,maxy = minmax(tiles, 1)
    return (
        int([k  for k,v in tiles.items() if v['coords'] == (minx,miny)][0]) *
        int([k  for k,v in tiles.items() if v['coords'] == (minx,maxy)][0]) *
        int([k  for k,v in tiles.items() if v['coords'] == (maxx,miny)][0]) *
        int([k  for k,v in tiles.items() if v['coords'] == (maxx,maxy)][0])
    , tiles)

def monster_hunter(img, monster):
    monster_length = max(monster, key=lambda m: m[0])[0]
    monster_height = max(monster, key=lambda m: m[1])[1]
    for j in range(len(img)-monster_height):
        for i in range(len(img[j])-monster_length):
            if all([img[j+m[1]][i+m[0]] in ['#', 'O'] for m in monster]):
                for b,a in [(j+m[1],i+m[0]) for m in monster]:
                    img[b][a] = 'O'
    return img

def part_two(inputs):
    tiles = part_one(inputs)[1]
    minx,maxx = minmax(tiles,0)
    miny,maxy = minmax(tiles,1)
    img = []
    for j in range(miny, maxy+1):
        tys = [y['tile'] for y in sorted([tile for tile in tiles.values() if tile['coords'][1] == j], key=lambda x: x['coords'][0])]
        for y in range(1,len(tys[0])-1):
            img.append(''.join([''.join(t[y][1:-1]) for t in tys]))
# MONSTER
                  # 
#    ##    ##    ###
 #  #  #  #  #  #    
    monster_in = open('inputs/20.2', 'r').readlines()
    monster = []
    for y in range(len(monster_in)):
        for x in range(len(monster_in[y])):
            if monster_in[y][x] == '#':
                monster += [(x,y)]
    
    for _ in range(4):
        img = monster_hunter(img, monster)
        img = flipx(img)
        img = monster_hunter(img, monster)
        img = flipx(img)
        img = rotate_clockwise(img)
    return sum(1 for y in ''.join([''.join(x) for x in img]) if y == '#')

s = start_time()
# print(part_one(open('inputs/20.1', 'r').read())[0]) 
print(part_one(open('inputs/20', 'r').read())[0])
end_time(s)

s = start_time()
# print(part_two(open('inputs/20.1', 'r').read())) 
print(part_two(open('inputs/20', 'r').read())) 
end_time(s)
