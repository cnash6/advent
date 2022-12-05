#!/usr/bin/env python

import re
import copy

def do_it(fname):
    with open(fname, 'r') as f:
        inputs = f.read()

    stacks_in, instructions = (x.split('\n') for x in inputs.split('\n\n'))

    # build initial stacks
    stacks = [list() for _ in stacks_in[-1].split('   ')]
    for i in reversed(range(len(stacks_in)-1)):
        for j in range(len(stacks)):
            if stacks_in[i][1+4*j] != ' ':
                stacks[j].append(stacks_in[i][1+4*j])
    stacks2 = copy.deepcopy(stacks)
    
    for instruction in instructions:
        num_moved, from_stack, to_stack = (int(x) for x in re.split(r'[a-zA-Z ]+', instruction.strip('move ')))
        for _ in range(num_moved):
            stacks[to_stack-1].append(stacks[from_stack-1].pop())
        
        stacks2[to_stack-1].extend(reversed(list(stacks2[from_stack-1].pop() for _ in range(num_moved))))

    return ''.join(x.pop() for x in stacks), ''.join(x.pop() for x in stacks2)

print(do_it("inputs/05.1"))
print(do_it("inputs/05"))

