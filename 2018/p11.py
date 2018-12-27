# !/usr/bin/env python
from collections import defaultdict

def print_cells(cells):
    for row in cells:
        print("\t".join(map(str,row)))

def get_power(i, j):
    rack_id = i + 10
    power = rack_id * j
    power = power + 8979
    power = power * rack_id
    power = power // 100 % 10
    power = power - 5
    return power

def get_partial_sum(x, y, partial_sums):
    return get_power(x + 1, y + 1) + partial_sums[x, y-1] + partial_sums[x-1, y] - partial_sums[x-1, y-1]

if __name__ == '__main__':
    
    #  Part 1
    N = 8979
    GRID_SIZE = 300
    
    cells = [[None] * GRID_SIZE for x in range(GRID_SIZE)]
    largest3 = (-float("inf"), None)
    for i in range(1, GRID_SIZE+1):
        for j in range(1, GRID_SIZE+1):
            cells[i-1][j-1] = get_power(i, j)
            if (i > 2 and j > 2):
                power = sum([sum(cells[i-x-1][j-3:j]) for x in range(0,3)])
                if (power > largest3[0]):
                    largest3 = (power, (i-2,j-2))
    print(largest3)

    # Part 2

    grid_sums =  {}
    partial_sums = defaultdict(int)

    for j in range(GRID_SIZE):
        for i in range(GRID_SIZE):
            partial_sums[(i, j)] = get_partial_sum(i, j, partial_sums)
    
    for size in range(2, GRID_SIZE):
        for j in range(size-1, GRID_SIZE):
            for i in range(size-1, GRID_SIZE):
                partial = partial_sums[(i, j)] + partial_sums[(i-size, j-size)] - partial_sums[(i-size, j)] - partial_sums[(i, j-size)]
                grid_sums[partial] = (i-size+2, j-size+2, size)
        
    print(grid_sums[max(grid_sums)])
