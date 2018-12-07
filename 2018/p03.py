# !/usr/bin/env python

def check_overlap(claim, vertexes):
    for i in range(0, claim[2][0]):
        for j in range(0, claim[2][1]):
            v = (claim[1][0]+i, claim[1][1]+j)
            if (len(vertexes[v]) > 1):
                return True
    return False

if __name__ == '__main__':
    f = open('assets/03.txt', 'r')
    claims = [[x[0], tuple(map(int, tuple(x[1].split(',')))), tuple(map(int, tuple(x[2].split('x'))))] for x in [[x[0]] + x[1].split(': ') for x in [x.rstrip().split(' @ ') for x in f]]]
    vertexes = {}
    count = 0

    # Part 1
    for claim in claims:
        for i in range(0, claim[2][0]):
            for j in range(0, claim[2][1]):
                v = (claim[1][0]+i, claim[1][1]+j)

                if v not in vertexes:
                    vertexes[v] = [claim[0]]
                else:
                    vertexes[v].append(claim[0])
                    if len(vertexes[v]) is 2:
                        count += 1

    print(f'number of overlaps: {count}')   

    #  Part 2
    for claim in claims:
        overlap = check_overlap(claim, vertexes)
        if not overlap:
            print(f'no overlap: {claim[0]}')
            

    



