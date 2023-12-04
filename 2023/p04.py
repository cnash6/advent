#!/usr/bin/env python

from utils import aocin

def do_it(inputs: list[str]):
    part1 = 0
    part2 = [1]*len(inputs)
    for i, numbers in enumerate(inputs):
        winners, card = numbers.split(" | ")
        winners = winners.split(": ")[1].split()
        card = card.split()
        
        card_winners = len(set([x for x in card if x in winners]))

        part1 += (2**(card_winners-1) if card_winners else 0)

        if card_winners:
            for j in range(1,card_winners+1):
                part2[i+j] += part2[i]

    return part1, sum(part2)

print(do_it(aocin("inputs/04.1")))
print(do_it(aocin("inputs/04")))




