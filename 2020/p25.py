#!/usr/bin/env python

from utils import *

def part_one(inputs):
    cardpublic,doorpublic = [int(x) for x in inputs]
    subject = 7
    divisor = 20201227
    val = 1
    cardprivate,doorprivate = 1,1
    while True:
        if val == cardpublic:
            return doorprivate
        if val == doorpublic:
            return cardprivate

        val = (val * subject) % divisor
        cardprivate = (cardprivate * cardpublic) % divisor
        doorprivate = (doorprivate * doorpublic) % divisor

s = start_time()
print(part_one(aocin('inputs/25.1')))
print(part_one(aocin('inputs/25')))
end_time(s)
