# !/usr/bin/env python
from collections import deque
from utils import check_progress

if __name__ == '__main__':
    f = open('assets/12.txt', 'r')
    
    #  Part 1
    start = [x.strip() for x in f]
    pots = [x for x in start[0][15:]]
    rules = dict([tuple(x.split(" => ")) for x in start[2:] if x[-1] == '#'])
    N = 120

    # print(rules)

    added_left = 0
    mysum = 0
    for n in range(N):
        # check_progress(n, N)
        first_plant = pots.index('#')
        r = pots[:]
        r.reverse()
        last_plant = r.index('#')
        added_left = added_left + 3-first_plant if first_plant < 3 else added_left
        pots = ['.' for x in range(3-first_plant)]+pots+['.' for x in range(3-last_plant)]
        next_gen = ['.' for x in range(len(pots))]
        for i in range(0, len(pots)-4):
            if "".join(pots[i:i+5]) in rules:
                next_gen[i+2] = '#'
        pots = next_gen[:]
        newsum = sum([x-added_left for x in range(len(pots)) if pots[x] == '#'])
        print(f'{newsum} : {newsum - mysum}')
        mysum = newsum
        

    print(sum([x-added_left for x in range(len(pots)) if pots[x] == '#']))









        