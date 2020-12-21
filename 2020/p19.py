#!/usr/bin/env python

from utils import *
import re

def build_regex(rule, rules):
    if rule[0] == '"':
        return rule[1:-1]
    return '('+'|'.join([f'{"".join([build_regex(rules[y.split("MOD")[0].strip()], rules)+(y.split("MOD")[1] if "MOD" in y else "") for y in x.split(" ")])}' for x in rule.split(' | ')])+')'


def part_one(inputs):
    rules,images = [x.split('\n') for x in inputs.split('\n\n')]
    rules = {x[0]: x[1] for x in [y.split(': ') for y in rules]}
    r = rf'{build_regex(rules["0"], rules)}'
    return sum(1 for x in images if re.fullmatch(r, x))

def part_two(inputs):
    rules,images = [x.split('\n') for x in inputs.split('\n\n')]
    rules = {x[0]: x[1] for x in [y.split(': ') for y in rules]}
    rules['8'] = '42MOD+'
    matches = []
    for n in range(1,20):
        x = '{' + str(n) + '}'
        rules['11'] = f'42MOD{x} 31MOD{x}'
        r = rf'{build_regex(rules["0"], rules)}'
        matches = matches + [1 for x in images if re.fullmatch(r, x)]
        print(len(matches))
    return sum(matches)
    

# s = start_time()
# print(part_one(open('inputs/19.1', 'r').read())) 
# print(part_one(open('inputs/19', 'r').read())) 
# end_time(s)


s = start_time()
print(part_two(open('inputs/19.2', 'r').read())) 
print(part_two(open('inputs/19', 'r').read())) 
end_time(s)
