#!/usr/bin/env python

from utils import aocin

def do_it(fname, n):
    with open(fname, 'r') as f:
        inputs = f.read()
    for i in range(len(inputs)-n):
        if len(set(inputs[i:i+n])) == n:
            return i+n

print(do_it("inputs/06.1", 4))
print(do_it("inputs/06", 4))

print(do_it("inputs/06.1", 14))
print(do_it("inputs/06", 14))