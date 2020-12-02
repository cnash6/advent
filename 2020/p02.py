#!/usr/bin/env python



def doit(input_file):
    f = open(input_file, 'r')
    policies =  [z[0].split('-') + z[1:] for z in [y[0].strip().split(' ') + [y[1].strip()] for y in [x.split(":") for x in f]]]
    good1, good2 = 0,0
    for policy in policies:
        occurences = [i for i, l in enumerate(policy[3]) if l == policy[2]]
        if len(occurences) >= int(policy[0]) and len(occurences) <= int(policy[1]):
            good1+=1
        if (policy[3][int(policy[0])-1] == policy[2] or policy[3][int(policy[1])-1] == policy[2]) and policy[3][int(policy[0])-1] != policy[3][int(policy[1])-1]:
            good2+=1
    return (good1, good2)

# Part One & two
print(doit('inputs/02.1'))
print(doit('inputs/02'))
