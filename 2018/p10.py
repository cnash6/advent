# !/usr/bin/env python
from collections import namedtuple
from utils import check_progress

def sim(lights):
    newlights = []
    # xmin ymin xmax ymax
    bounds = [float('inf'), float('inf'), -float('inf'), -float('inf')]
    for l in lights:
        nl = Light(P(l.p.x + l.v.dx, l.p.y + l.v.dy), V(l.v.dx, l.v.dy))
        newlights.append(nl)
        if nl.p.x < bounds[0]:
            bounds[0] = nl.p.x
        if nl.p.y < bounds[1]:
            bounds[1] = nl.p.y
        if nl.p.x > bounds[2]:
            bounds[2] = nl.p.x
        if nl.p.y > bounds[3]:
            bounds[3] = nl.p.y
    return (newlights, bounds)

def area(v):
    return abs(v[0] - v[2])*abs(v[1] - v[3])

def print_it(i, lights):
    map = [[' '] * 200 for j in range(150)]
    for l in lights:
        map[l.p.y + i * l.v.dy - 200][l.p.x + i * l.v.dx - 150] = '*'

    for m in map:
        print(''.join(m))

if __name__ == '__main__':
    f = open('assets/10.txt', 'r')
    
    #  Part 1
    P = namedtuple('pos', 'x y')
    V = namedtuple('vel', 'dx dy')
    Light = namedtuple('light', 'p v')

    lights = [Light(P(*map(int,x[0].strip().split(','))), V(*map(int,x[1].strip().split(',')))) for x in [x.strip()[10:-1].split('>velocity=<') for x in f]]
    orig_lights = lights[:]
    N = 11000
    smallest = (0, float('inf'), None)
    for i in range(N):
        check_progress(i, N)
        lights, bounds = sim(lights)
        # print(bounds)
        a = area(bounds)
        # print(a)
        if a < smallest[1]:
            smallest = (i+1, a, bounds)
    
    print(smallest)
    print_it(smallest[0], orig_lights)

        