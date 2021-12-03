#!/usr/bin/env python

from utils import *


def part_one(inputs):
    a = [0]*len(inputs[0])
    for thing in inputs:
        a = [a[i]+int(thing[i]) for i in range(len(thing))]
    a = ''.join(['1' if x>len(inputs)/2 else '0' for x in a])
    b = ''.join(['0' if int(x) else '1' for x in a])
    return int(a,2)*int(b,2)

def part_two(inputs):
    oxy = inputs[:]
    i = 0
    while len(oxy) > 1 and i < len(oxy[0]):
        ones,zeros = [],[]
        for o in oxy:
            if o[i] == '1':
                ones.append(o)
            else: 
                zeros.append(o)
        oxy = ones if len(ones) >= len(zeros) else zeros
        i+=1
    
    co2 = inputs[:]
    i = 0
    while len(co2) > 1 and i < len(co2[0]):
        ones,zeros = [],[]
        for o in co2:
            if o[i] == '1':
                ones.append(o)
            else: 
                zeros.append(o)
        co2 = ones if len(ones) < len(zeros) else zeros
        i+=1

    return int(oxy[0],2)*int(co2[0],2)


print(part_one(aocin("inputs/03.1")))
print(part_one(aocin("inputs/03")))

print(part_two(aocin("inputs/03.1")))
print(part_two(aocin("inputs/03")))
