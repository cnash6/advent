#!/usr/bin/env python

from utils import *
import re

def doit(inputs, fields): 
    acc1, acc2, reqd = 0, 0, set([x for x in fields.keys()])
    for passport in [x.replace('\n',' ').replace(' ', ',') for x in inputs.split('\n\n')]:
        if not reqd <= set([x.split(':')[0] for x in passport.split(',')]):
            continue
        acc1+=1

        pdict = dict([z.split(':') for z in passport.split(',')])
        acc2+= 1 if all([fields[field](pdict[field]) for field in fields]) else 0 
    return acc1, acc2

fields = {
    'byr': lambda x: re.fullmatch(r'\d{4}', x) and int(x) <= 2002, # (Birth Year)
    'iyr': lambda x: re.fullmatch(r'\d{4}', x) and 2010 <= int(x) <= 2020, # (Issue Year)
    'eyr': lambda x: re.fullmatch(r'\d{4}', x) and 2020 <= int(x) <= 2030, # (Expiration Year)
    'hgt': lambda x: re.fullmatch(r'\d+(cm|in)', x) and (150 <= int(x[:-2]) <= 193 if x[-2:] == 'cm' else 59 <= int(x[:-2]) <= 76), # (Height)
    'hcl': lambda x: re.fullmatch(r'#([\da-z]){6}', x), # (Hair Color)
    'ecl': lambda x: re.fullmatch(r'amb|blu|brn|gry|grn|hzl|oth', x), # (Eye Color)
    'pid': lambda x: re.fullmatch(r'\d{9}', x) # (Passport ID)
    # 'cid': False # (Country ID) NO
}

# Part One 
print(doit(open('inputs/04.1', 'r').read(), fields))
print(doit(open('inputs/04.2', 'r').read(), fields))
print(doit(open('inputs/04', 'r').read(), fields))

