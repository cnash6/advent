# !/usr/bin/env python

def destroy_pairs(polymer):
    i = 0
    while i < len(polymer) - 1:
        if polymer[i] != polymer[i+1] and polymer[i].upper() == polymer[i+1].upper():
            polymer = polymer[:i] + polymer[i+2:]
            i = i-1 if i > 0 else 0
        else:
            i+=1
    return polymer

if __name__ == '__main__':
    f = open('assets/05.txt', 'r')
    
    #  Part 1
    polymer = f.read().strip()
    removed = destroy_pairs(polymer)

    print(f'resulting length: {len(removed)}')

    # Part 2
    units = sorted(set(polymer.upper()))
    shortest = None
    for u in units:
        new_polymer = [x for x in polymer if x != u and x != u.lower()]
        removed = (u, len(destroy_pairs(new_polymer)))
        print(removed)
        if not shortest or removed[1] < shortest[1]:
            shortest = removed
        
    print(f'shortest molecule after removing {shortest[0]}: {shortest[1]}')
        



