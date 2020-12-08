#!/usr/bin/env python

from utils import *

def contains_target(bag, target, containers):
    if containers[bag] == True or list(filter(lambda b: b[1] == target, containers[bag])):
        containers[bag] = True
        return True, containers
    for child in [x for x in containers[bag] if x != (0, 'None')]:
        contains, containers = contains_target(child[1], target, containers)
        if contains:
            containers[bag] = True
            return True, containers
    return False, containers

def count_bags(bag, containers):
    return 1 + sum([numchild * count_bags(child, containers) for numchild, child, in containers[bag] if child != 'None'])

def parse_bags(inputs):
    return {y[0]: [(int(w[0]), w[1]) for w in [z.split(' ', 1) for z in y[1].replace(' bags', '').replace(' bag', '').split(', ')]] if y[1] != 'no other bags' else [(0, 'None')] for y in [x[:-1].split(' bags contain ') for x in inputs]}

def part_one(inputs, target): 
    containers = parse_bags(inputs)
    return sum([1 for x in containers.keys() if contains_target(x, target, containers)[0]])

def part_two(inputs, target): 
    containers = parse_bags(inputs)
    return count_bags(target, containers)-1

# Part One 
print(part_one(aocin('inputs/07.1'), 'shiny gold'))
print(part_one(aocin('inputs/07'), 'shiny gold'))

# Part Two 
print(part_two(aocin('inputs/07.1'), 'shiny gold'))
print(part_two(aocin('inputs/07.2'), 'shiny gold'))
print(part_two(aocin('inputs/07'), 'shiny gold'))