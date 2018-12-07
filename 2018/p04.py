# !/usr/bin/env python
from collections import defaultdict

def get_sleepiest_minute(minutes):
    min_counts = defaultdict(int)
    for minute in minutes:
        min_counts[minute[1]] +=1
    return sorted(list(min_counts.items()), key=lambda k: -k[1])[0]


if __name__ == '__main__':
    f = open('assets/04.txt', 'r')

    #  Part 1
    records = sorted([[x[0][1:]] + x[1].split(' ') for x in [x.split('] ') for x in [x.rstrip() for x in f]]], key=lambda k: k[0]) 

    guards = defaultdict(list)
    active = None
    start = None

    for r in records:
        if r[1] == 'Guard':
            active = r[2]
        if r[1] == 'falls':
            start = r[0].split(':')[1]
        if r[1] == 'wakes':
            guards[active] = guards[active] + [(r[0].split(' ')[0], x) for x in range(int(start), int(r[0].split(':')[1]))]

    sleepiest = sorted(list(guards.items()), key=lambda k: -len(k[1]))[0]

    sleepiest_guard = sleepiest[0]
    sleepiest_minute = get_sleepiest_minute(sleepiest[1])
    print(f'worst guard: {sleepiest_guard}')
    print(f'worst minute: {sleepiest_minute}')
    print(f'solution: {int(sleepiest_guard[1:]) * int(sleepiest_minute[0])}')

    #  Part 2
    worst_mins = map(lambda k: (k[0], get_sleepiest_minute(k[1])), list(guards.items()))

    worst_min_for_all = sorted(worst_mins, key=lambda k: -k[1][1])[0]
    print(f'worst min for all: guard {worst_min_for_all[0][1:]} at min {worst_min_for_all[1][0]} => {int(worst_min_for_all[0][1:])*int(worst_min_for_all[1][0])}')

    



