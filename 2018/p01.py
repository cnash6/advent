# !/usr/bin/env python

def getFirstMatch(changes):
    i = 0
    drift = 0
    searching = True
    frequencies = []
    frequencies.append(0)
    while searching:
        drift+=changes[i]
        if drift in frequencies:
            return drift
        else: 
            frequencies.append(drift)
        i = i+1 if i < len(changes)-1 else 0


if __name__ == '__main__':
    f = open('assets/01.txt', 'r')
    changes = [int(x.rstrip()) for x in f]
    
    # Part 1
    drift = 0
    for change in changes:
        drift+=change
    
    print(f'total drift: {drift}')

    # part 2

    match = getFirstMatch(changes)
    print(f'first match {match}')

        


