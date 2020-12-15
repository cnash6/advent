#!/usr/bin/env python

from utils import *

def part_one(inputs):
    mem = {}
    maskon,maskoff = None,None
    for inn in inputs:
        if inn[:3] == 'mem':
            addr, val = inn.split(' = ')
            mem[addr[4:-1]] = (int(val) | maskon) & maskoff
        else:
            mask = [x for x in inn[7:]]
            maskon = int(''.join(['1' if x == '1' else '0' for x in mask]), 2)
            maskoff = int(''.join(['0' if x == '0' else '1' for x in mask]), 2)

    return sum([x for x in mem.values()])

def part_two(inputs):
    mem = {}
    mask = None
    for inn in inputs:
        if inn[:3] == 'mem':
            addr, val = inn.split(' = ')[0][4:-1],  int(inn.split(' = ')[1])
            addrs = [int(addr) | int(''.join(['1' if x == '1' else '0' for x in mask]), 2)]
            for floating in [int(i) for i,x in enumerate(mask) if x == 'X']:
                addrs = [a | int(''.join(['1' if i == floating else '0' for i in range(36)]),2) for a in addrs] + [a & int(''.join(['0' if i == floating else '1' for i in range(36)]),2) for a in addrs]
            mem = mem | {a: val for a in addrs}
        else:
            mask = [x for x in inn[7:]]

    return sum([x for x in mem.values()])

s = start_time()
print(part_one(aocin('inputs/14.1')))
print(part_one(aocin('inputs/14')))
end_time(s)

s = start_time()
print(part_two(aocin('inputs/14.2')))
print(part_two(aocin('inputs/14')))
end_time(s)