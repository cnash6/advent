#!/usr/bin/env python

from utils import *

instructions = {
    'acc': lambda n,a,i: (a + int(n), i+1),
    'jmp': lambda n,a,i: (a, i+int(n)),
    'nop': lambda n,a,i: (a, i+1)
}

def runcode(code):
    acc,i = 0,0
    
    history = []
    while True:
        if i >= len(code):
            return (0, acc)
        if i in history:
            return (1, acc)
        history.append(i)
        acc,i = instructions[code[i][0]](code[i][1], acc, i)
    
def part_one(inputs):
    code = [(y[0], int(y[1])) for y in [x.split(' ') for x in inputs]]
    return runcode(code)
    
def part_two(inputs):
    code = [(y[0], int(y[1])) for y in [x.split(' ') for x in inputs]]
    for i, c in enumerate(code):
        if c[0] != 'acc':
            newcode = code[:]
            newcode[i] = ('jmp', code[i][1]) if c == 'nop' else ('nop', code[i][1])
            err,res = runcode(newcode)
            if not err:
                return i,res
    return 'fail'

# Part One 
print(part_one(aocin('inputs/08.1')))
print(part_one(aocin('inputs/08')))

# Part Two 
print(part_two(aocin('inputs/08.1')))
print(part_two(aocin('inputs/08')))
