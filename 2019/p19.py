#!/usr/bin/env python
# coding: utf-8

from shared.intcode import *

# Main      
f = open('assets/19.txt', 'r')
intcode = [int(x) for x in f.read().rstrip().split(',')]

def print_graph(graph):
    min_x = min(x for x, _ in graph)
    min_y = min(y for _, y in graph)
    max_x = max(x for x, _ in graph)
    max_y = max(y for _, y in graph)
    print("\n".join(("".join(str(graph[(x, y)]) for x in range(min_x, max_x + 1))) for y in range(min_y, max_y + 1)) + '\n')

N = 50
comp = Computer(intcode)
locations = [(x,y) for x in range(N) for y in range(N)]
outputs = {}

asum = 0
for loc in locations:
    comp = Computer(list(intcode), [0]+list(loc)) # why in the world I need a 0 as the first input, I don't know, but it reads 3 inputs instead of 2
    comp.run_program()
    outputs[loc] = comp.outputs[0]
    asum +=comp.outputs[0]

print_graph(outputs)
print(asum)
