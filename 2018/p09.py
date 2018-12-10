# !/usr/bin/env python
from utils import check_progress
from collections import deque, defaultdict
from datetime import datetime


if __name__ == '__main__':
    startTime = datetime.now()
    NPLAYERS = 459
    N = 71790*100
    
    #  Part 1
    circle = deque([0])
    players = defaultdict(int)

    for i in range(1, N+1):
        # check_progress(i, N+1)
        if i % 23 == 0:
            circle.rotate(7)
            players[i % NPLAYERS] += i + circle.pop()
            circle.rotate(-1)
        else:
            circle.rotate(-1)
            circle.append(i)
    
    print(f'max score: {max(players.values())}')
    print(f'finished in {(datetime.now() - startTime).total_seconds()} seconds')