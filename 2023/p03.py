#!/usr/bin/env python

from utils import aocin

def do_it(inputs: list[str]):
    parts = []

    for j in range(len(inputs)):
        i = 0
        while i < len(inputs[j]):
            z = 0 
            found = None
            while i+z < len(inputs[j]):
                if inputs[j][i:i+z+1].isnumeric():
                    found = inputs[j][i:i+z+1]
                else:
                    break
                z+=1

            if found:
                adjacencies = [a for b in [[(i+k, j-1), (i+k, j), (i+k, j+1)] for k in range(-1, len(found)+1)] for a in b]
                if any([(not inputs[y][x].isnumeric() and inputs[y][x] != '.') for x,y in adjacencies if 0 <= x < len(inputs[0]) and 0 <= y < len(inputs)]):
                    parts.append((found, [(i+c,j) for c in range(len(found))]))
                
            i+=z+1
    print("p1:")
    print(sum(int(x[0]) for x in parts))

    p2 = 0
    for j in range(len(inputs)):
        for i in range(len(inputs[j])):
            if inputs[j][i] == '*':
                adj_ps = set()
                for adj in [(i-1,j-1), (i,j-1), (i+1,j-1), (i-1,j), (i+1,j), (i-1,j+1), (i,j+1), (i+1,j+1)]:
                    for part in parts:
                        if any([p == adj for p in part[1]]):
                            adj_ps.add(part[0])
                
                if len(adj_ps) == 2:
                    a,b = list(adj_ps)
                    p2 += int(a) * int(b)

    print("p2:")
    print(p2)



print(do_it(aocin("inputs/03.1")))
print(do_it(aocin("inputs/03")))




