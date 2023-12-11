#!/usr/bin/env python

from functools import reduce

def do_it(fname: str):
    with open(fname, 'r') as f:
        inputs = f.readlines()
    t,d = [x.strip().split(": ")[1].split() for x in inputs]
    races = [(int(t[i]), int(d[i]))for i in range(len(t))]
    
    winners = []
    for race in races:
        n = 0
        for i in range(race[0]):
            d = i*(race[0]-i)
            if d > race[1]:
                n+=1
        winners.append(n)
    
    return reduce(lambda x,y: x*y,winners)


def do_it2(fname: str):
    with open(fname, 'r') as f:
        inputs = f.readlines()
    t,d = [int(''.join(x.strip().split(": ")[1].split())) for x in inputs]

    n = 0
    for i in range(t):
        x = i*(t-i)
        if x > d:
            n+=1
    return n
    


        
# print(do_it("inputs/06.1"))
# print(do_it("inputs/06"))

print(do_it2("inputs/06.1"))
print(do_it2("inputs/06"))