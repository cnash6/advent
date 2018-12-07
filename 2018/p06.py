# !/usr/bin/env python
from collections import defaultdict

def manhattan(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

if __name__ == '__main__':
    f = open('assets/06.txt', 'r')
    
    #  Part 1
    points = [tuple(map(int, x.strip().split(', '))) for x in f]
    max_x = max([x[0] for x in points])
    min_x = min([x[0] for x in points])
    max_y = max([x[1] for x in points])
    min_y = min([x[1] for x in points])
    
    graph = defaultdict(list)
    safe = []

    for i in range(min_x, max_x+1):
        for j in range(min_y, max_y+1):
            distance = 0
            closest = None
            for point in points:
                man = manhattan((i,j), point)
                distance += man
                if closest == None:
                    closest = (point, man)
                elif closest[1] == man:
                    closest = ('#', man)
                elif closest[1] > man:
                    closest = (point, man)
            graph[closest[0]].append((i,j))
            if int(distance) < 10000:
                safe.append((i,j))

    # remove infinite ones (points on the edges)
    edges_removed = list(filter(lambda k: k != "#" and k[0] != min_x and k[0] != max_x and k[1] != min_y and k[1] != max_y, graph))

    largest = None
    for point in edges_removed:
        if largest == None or len(graph[point]) > largest[1]:
            largest = (point, len(graph[point]))
    
    print(largest)
    print(len(safe))
        



